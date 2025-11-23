from py4godot.classes import gdclass
from py4godot.classes.Node2D import Node2D
from py4godot.classes.core import NodePath


@gdclass
class InfoManager(Node2D):

	PetName: str = ""
	PetAge: int = 0
	PetType: str = ""
