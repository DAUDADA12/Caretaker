from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from py4godot.classes.core import NodePath 

@gdclass
class Pet_DATA_UI(Control):
    Age_Label : NodePath = NodePath()