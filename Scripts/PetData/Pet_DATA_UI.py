from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from py4godot.classes.core import NodePath 
from py4godot.classes.Slider import Slider

@gdclass
class Pet_DATA_UI(Control):
    Age_Label_Node : NodePath = NodePath()
    Name_Label_Node : NodePath = NodePath()
    Hunger_Bar_Node : NodePath = NodePath()
    Happiness_Bar_Node : NodePath = NodePath()
    
    Age_Label = None
    Name_Label = None
    Hunger_Bar = None
    Happiness_Bar = None

    def _ready(self):
        if(self.Age_Label_Node):
            self.Age_Label = self.get_node(self.Age_Label_Node)
        
        if(self.Name_Label_Node):
            self.Name_Label = self.get_node(self.Name_Label_Node)
        
        if(self.Hunger_Bar_Node):
            self.Hunger_Bar = self.get_node(self.Hunger_Bar_Node)