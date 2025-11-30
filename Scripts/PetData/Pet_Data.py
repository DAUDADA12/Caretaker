from py4godot.classes import gdclass
from py4godot.classes.Node import Node
from py4godot.classes.core import NodePath

@gdclass
class Pet_Data(Node):
	Name: str = ""
	Age: int = 0
	Hunger: int = 0
	Happines: float = 0
	Info_Manager: NodePath = NodePath()

	rate_of_change_of_age = 0.3
	rate_of_change_of_hunger = 0.4
	rate_of_change_of_happiness = 0.5

	info_manager_script = None

	Data = {}

	def _ready(self):
		if(self.Info_Manager):
			self.info_manager_script = self.get_node(self.Info_Manager).get_pyscript()
			self.Data = self.info_manager_script.load_data()
			print("This is the data loaded:",self.Data)
		self.Age = self.Data.get("petAge")
		self.Hunger = self.Data.get("petHunger")
		self.Happines = self.Data.get("petEnergy")
	
	def _process(self, delta):
		self.Age += self.rate_of_change_of_age * delta
		self.Happines -= self.rate_of_change_of_happiness * delta
		self.Hunger -= self.rate_of_change_of_hunger * delta
