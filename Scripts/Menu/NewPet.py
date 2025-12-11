from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.OptionButton import OptionButton
from py4godot.classes.core import NodePath

@gdclass
class NewPet(OptionButton):

    Data = {
        "petName": '',
        "petType": -1,
        "petHunger": 100,
        "petHappines": 100,
        "petEnergy": 100,
        "petHealth": 100,
        "petCleanliness": 100,
        "petRest": 100,
        "petAge": 0
    }

    DogList_Node: NodePath = NodePath()
    CatList_Node: NodePath = NodePath()
    Submit_Button_Node: NodePath = NodePath()
    InfoManager: NodePath = NodePath()

    DogList = None
    CatList = None
    SubmitButton = None
    info_manager_py = None

    MAIN_SCENE = "res://Scenes/MainScene.tscn"  # Path to main scene

    def _ready(self):
        self.info_manager_py = self.get_node(self.InfoManager).get_pyscript()

        if self.Submit_Button_Node:
            self.SubmitButton = self.get_node(self.Submit_Button_Node)

        if self.CatList_Node:
            self.CatList = self.get_node(self.CatList_Node)

        if self.DogList_Node:
            self.DogList = self.get_node(self.DogList_Node)

    def OnPetTypeSelected(self, index: int):
        self.DogList.visible = index == 0
        self.CatList.visible = index == 1
        self.Scan()

    def OnDogSelected(self, index: int):
        if self.DogList.visible:
            self.Data["petType"] = index  # 0 or 1
        self.Scan()

    def OnCatSelected(self, index: int):
        if self.CatList.visible:
            self.Data["petType"] = index + 2  # 2 or 3
        self.Scan()

    def Scan(self):
        print(self.Data)
        self.SubmitButton.visible = (
            self.Data["petName"] != '' and self.Data["petType"] in range(0, 4)
        )

    def OnNameEntered(self, new_text: str):
        self.Data["petName"] = new_text
        self.Scan()

    def OnSubmit(self):
        if self.info_manager_py:
            # Save the pet data
            self.info_manager_py.save_data(self.Data)
            print("Pet data saved!")

        # Redirect to main scene
        tree = self.get_tree()
        if tree:
            tree.change_scene_to_file(self.MAIN_SCENE)
            print(f"Redirected to {self.MAIN_SCENE}")
        else:
            print("Error: SceneTree not found")
