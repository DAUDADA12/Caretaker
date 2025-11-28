from py4godot.classes import gdclass
from py4godot.classes.Node2D import Node2D
from py4godot.classes.core import NodePath

@gdclass
class InfoManager(Node2D):

	NodeName: NodePath = NodePath()  # Assigned in Inspector
	print("Test")

	def _ready(self):
		print("It works")
		# Get the Godot node
		global node
		node = self.get_node(self.NodeName)

		# Get the Python script attached to it
		py_script = node.get_pyscript()

		if py_script:
			py_script.update_status()  # Call method from InfoHandler.py
		else:
			print("No Python script found on the node!")
	
	def _process(self, delta):
		py_script = node.get_pyscript()
