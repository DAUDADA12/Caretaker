from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node import Node
from py4godot.classes.core import NodePath

@gdclass
class play(Node):
	Pet_Info: NodePath = NodePath()
	pet_info_node = None
	pet_info_script = None
	
	def _ready(self):
		self.pet_info_node = self.get_node(self.Pet_Info)
		self.pet_info_script = self.pet_info_node.get_pyscript()
	def feed(self, amount: int):
		self.pet_info_script.Happines += amount


	def _on_pressed(self):
		if(self.pet_info_script.Happines < 100):
			self.feed(10)
		else:
			self.pet_info_script.Happines = 100
