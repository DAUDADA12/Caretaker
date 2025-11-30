from py4godot.classes import gdclass
from py4godot.classes.Node import Node
from py4godot.classes.core import NodePath

@gdclass
class Pet_Data(Node):
	Name: str = ""
	Age: int = 0
	Hunger: float = 0
	Happines: float = 0
	Energy: int = 0
	Health: int = 0
	Cleanliness: int = 0
	Info_Manager: NodePath = NodePath()

	rate_of_change_of_age = 0.3
	rate_of_change_of_hunger = 0.4
	rate_of_change_of_happiness = 0.5
	rate_of_change_of_health = 1.2
	rate_of_change_of_cleanliness = 0.2
	rate_of_change_of_energy = 0.5

	info_manager_script = None

	Data = {}

	def _ready(self):
		if(self.Info_Manager):
			self.info_manager_script = self.get_node(self.Info_Manager).get_pyscript()
			self.Data = self.info_manager_script.load_data()
			print("This is the data loaded:",self.Data)
		self.Age = self.Data.get("petAge")
		self.Hunger = self.Data.get("petHunger")
		self.Happines = self.Data.get("petHappines")
		self.Energy = self.Data.get("petEnergy")
		self.Health = self.Data.get("petHealth")
		self.Cleanliness = self.Data.get("petCleanliness")
	
	def _process(self, delta):
		self.Age += self.rate_of_change_of_age * delta
		self.Happines -= self.rate_of_change_of_happiness * delta
		self.Hunger -= self.rate_of_change_of_hunger * delta
		self.Cleanliness -= self.rate_of_change_of_cleanliness * delta
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
		else:
			if not taking_damage and self.Hunger > 20 and self.Happines > 20 and self.Cleanliness > 20 and self.Energy > 20 and self.Health < 100:
				self.Health += self.rate_of_change_of_health * delta

	def _exit_tree(self):
		self.Data["petAge"] = self.Age
		self.Data["petHunger"] = self.Hunger
		self.Data["petEnergy"] = self.Happines
		if(self.info_manager_script):
			self.info_manager_script.save_data(self.Data)
	
