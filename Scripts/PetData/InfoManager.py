from py4godot.classes import gdclass
from py4godot.classes.Node2D import Node2D
from py4godot.classes.core import NodePath
from py4godot import private


@gdclass
class InfoManager(Node2D):

	PetName: str = ""
	PetAge: int = 0
	PetType: str = ""
	PetHappines: int = 0
	PetCleanlines: int = 100
	PetHunger: int = 0
	PetEnergy: int = 0
