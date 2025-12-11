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
	Health_Bar_Node : NodePath = NodePath()
	Cleanliness_Bar_Node : NodePath = NodePath()
	Type_Lable_Node : NodePath = NodePath()
	PetInfo_Node : NodePath = NodePath()
	Energy_Bar_Node : NodePath = NodePath()
	
	Age_Label = None
	Energy_Bar = None
	Type_Label = None
	Name_Label = None
	Hunger_Bar = None
	Happiness_Bar = None
	Pet_Info = None
	Health_Bar = None
	Cleanliness_Bar = None
	pet_info_py = None

	def _ready(self):
		if(self.Age_Label_Node):
			self.Age_Label = self.get_node(self.Age_Label_Node)
		if(self.Name_Label_Node):
			self.Name_Label = self.get_node(self.Name_Label_Node)
		if(self.Hunger_Bar_Node):
			self.Hunger_Bar = self.get_node(self.Hunger_Bar_Node)
		if(self.Happiness_Bar_Node):
			self.Happiness_Bar = self.get_node(self.Happiness_Bar_Node)
		if(self.Type_Lable_Node):
			self.Type_Label = self.get_node(self.Type_Lable_Node)
		if(self.PetInfo_Node):
			self.Pet_Info = self.get_node(self.PetInfo_Node)
			self.pet_info_py = self.Pet_Info.get_pyscript()
		if(self.Health_Bar_Node):
			self.Health_Bar = self.get_node(self.Health_Bar_Node)
		if(self.Cleanliness_Bar_Node):
			self.Cleanliness_Bar = self.get_node(self.Cleanliness_Bar_Node)
		if(self.Energy_Bar_Node):
			self.Energy_Bar = self.get_node(self.Energy_Bar_Node)

		self.Name_Label.text = "Name: " + self.pet_info_py.Data.get("petName")
		self.Age_Label.text = "Age: " + str(round(self.pet_info_py.Data.get("petAge"),2))
		
		if(self.pet_info_py.Data.get("petType") == 0):
			self.Type_Label.text = "Type: Gemran Shepherd"
		elif(self.pet_info_py.Data.get("petType") == 1):
			self.Type_Label.text = "Text: Iba Shinu"
		elif(self.pet_info_py.Data.get("petType") == 2):
			self.Type_Label.text = "Type: Orange Cat"
		elif(self.pet_info_py.Data.get("petType") == 3):
			self.Type_Label.text = "Type: Black Cat"

	def _process(self, delta):
		self.Age_Label.text = "Age: " + str(round(float(self.pet_info_py.Age), 1))
		self.Hunger_Bar.value = self.pet_info_py.Hunger
		self.Happiness_Bar.value = self.pet_info_py.Happines
		self.Health_Bar.value = self.pet_info_py.Health
		self.Cleanliness_Bar.value = self.pet_info_py.Cleanliness
		self.Energy_Bar.value = self.pet_info_py.Energy
