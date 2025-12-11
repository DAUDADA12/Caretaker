from py4godot.classes import gdclass
from py4godot.classes.Node import Node
from py4godot.classes.core import NodePath

@gdclass
class Pet_Data(Node):
	Name: str = ""
	Age: int = 0
	Type: int = 0
	Hunger: float = 0
	Happines: int = 0
	Energy: int = 0
	Health: int = 0
	Cleanliness: float = 0
	Rest: float = 0

	Info_Manager: NodePath = NodePath()
	DeathUI_Path: NodePath = NodePath()
	German_Shephard: NodePath = NodePath()
	Shiba_Inu: NodePath = NodePath()
	OrangeCat: NodePath = NodePath()
	BlackCat: NodePath = NodePath()

	rate_of_change_of_age = 0.3
	rate_of_change_of_hunger = 0.4
	rate_of_change_of_happiness = 0.5
	rate_of_change_of_health = 1.2
	rate_of_change_of_cleanliness = 0.5
	rate_of_change_of_energy = 0.6

	info_manager_script = None
	DeathUI = None
	Data = {}

	def _ready(self):


		# LOAD INFO MANAGER
		self.DeathUI = self.get_node(self.DeathUI_Path)

		if self.Info_Manager:
			self.info_manager_script = self.get_node(self.Info_Manager).get_pyscript()
			self.Data = self.info_manager_script.load_data()
			print("This is the data loaded:", self.Data)

		# LOAD PET STATS
		self.Name        = self.Data.get("petName", "Saiman")
		self.Age         = self.Data.get("petAge", 0)
		self.Type        = self.Data.get("petType", 0)
		self.Hunger      = self.Data.get("petHunger", 100)
		self.Happines    = self.Data.get("petHappines", 100)
		self.Energy      = self.Data.get("petEnergy", 100)
		self.Health      = self.Data.get("petHealth", 100)
		self.Cleanliness = self.Data.get("petCleanliness", 100)
		self.Rest        = self.Data.get("petRest", 100)
		
		# VISIBILITY FOR PET TYPE
		if self.Type == 0:
			self.get_node(self.German_Shephard).visible = True
		elif self.Type == 1:
			self.get_node(self.Shiba_Inu).visible = True
		elif self.Type == 2:
			self.get_node(self.OrangeCat).visible = True
		elif self.Type == 3:
			self.get_node(self.BlackCat).visible = True

	def _process(self, delta):
		self.Age += self.rate_of_change_of_age * delta
		self.Happines -= self.rate_of_change_of_happiness * delta
		self.Hunger -= self.rate_of_change_of_hunger * delta
		self.Cleanliness -= self.rate_of_change_of_cleanliness * delta
		self.Energy -= self.rate_of_change_of_energy * delta

		taking_damage = False

		if self.Hunger <= 0:
			self.Health -= self.rate_of_change_of_health * delta
			taking_damage = True

		if self.Happines <= 0:
			self.Health -= self.rate_of_change_of_health * delta
			taking_damage = True

		if self.Cleanliness <= 0:
			self.Health -= self.rate_of_change_of_health * delta
			taking_damage = True

		if self.Energy <= 0:
			self.Health -= self.rate_of_change_of_health * delta
			taking_damage = True

		# AUTO HEAL
		if not taking_damage and self.Hunger > 20 and self.Happines > 20 and self.Cleanliness > 20 and self.Energy > 20 and self.Health < 100:
			self.Health += self.rate_of_change_of_health * delta

		# DEATH LOGIC
		if self.Health <= 0:
			self.Health = 0
			self.DeathUI.visible = True
			self.Hunger = 0
			self.Happines = 0
			self.Energy = 0
			self.Cleanliness = 0
			self.Rest = 0

	def _exit_tree(self):
		# SAVE ALL DATA ON EXIT
		self.Data["petAge"] = self.Age
		self.Data["petHunger"] = self.Hunger
		self.Data["petEnergy"] = self.Energy
		self.Data["petHappines"] = self.Happines
		self.Data["petCleanliness"] = self.Cleanliness
		self.Data["petHealth"] = self.Health
		self.Data["petRest"] = self.Rest

		if self.info_manager_script:
			self.info_manager_script.save_data(self.Data)
	def _on_button_pressed(self):
		if self.info_manager_script:
			self.info_manager_script.delete_save()
		# Redirect safely
		self.go_to_main_menu()

	def go_to_main_menu(self):
		MAINMENU = "res://Scenes/MainMenu.tscn"
		tree = self.get_tree()
		if tree:
			tree.change_scene_to_file(MAINMENU)####
