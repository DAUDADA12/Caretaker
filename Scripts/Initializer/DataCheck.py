import os
from py4godot.classes.Node import Node
from py4godot.classes import gdclass
from py4godot.classes.core import NodePath
@gdclass
class DataCheck(Node):
	NewPetMenu: NodePath = NodePath()

	SAVE_PATH = "save_data.json"  # Save file path
	MAIN_SCENE = "res://Scenes/MainScene.tscn"  # Path to main scene

	def _ready(self):
		Menu = self.get_node(self.NewPetMenu)
		if self.save_exists():
			print("Save file exists → loading main scene")
			# Deferred call ensures SceneTree is ready
			self.call_deferred("load_main_scene")
		else:
			print("No save file found → stay on start screen")
			Menu.visible = True
	def save_exists(self) -> bool:
		return os.path.exists(self.get_save_path())

	# Get full path to the save file
	def get_save_path(self) -> str:
		base = os.getcwd()
		return os.path.join(base, self.SAVE_PATH)
	def load_main_scene(self):
		tree = self.get_tree()
		if tree:
			tree.change_scene_to_file(self.MAIN_SCENE)#Loading back to main menu.......