from py4godot.classes import gdclass
from py4godot.classes.Node import Node
from py4godot.classes.core import NodePath

@gdclass
class Pet_Data(Node):
	Name: str = ""
	Age: int = 0
	Hunger: int = 0

	Age_Node: NodePath = NodePath()
	Age_Label = None

	rate_of_change_of_age = 0.3

	def _ready(self):
		self.Age_Label = self.get_node(self.Age_Node)
	
	def _process(self, delta):
		self.Age += self.rate_of_change_of_age * delta
		print(self.Age)
		self.Age_Label.text = "Age:" + str(int(self.Age))