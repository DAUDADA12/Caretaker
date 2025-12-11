import json
import os
from py4godot.classes.Node2D import Node2D
from py4godot.classes import gdclass

@gdclass
class Data_Puller(Node2D):

    SAVE_FILENAME = "save_data.json"

    DEFAULT_SAVE = {
        'petName': '',
        'petAge': 0,
        'petHunger': 100,
        'petEnergy': 100,
        'petType': 0,
        'petHappines': 100,
        'petCleanliness': 100,
        'petHealth': 100,
        'petRest': 100
    }

    def _ready(self):
        print("SaveManager ready!")
        print("Save path:", self.get_save_path())

    def get_save_path(self) -> str:
        # Use folder of this script for a consistent save location
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, self.SAVE_FILENAME)

    def save_data(self, data: dict):
        try:
            with open(self.get_save_path(), "w") as f:
                json.dump(data, f, indent=4)
            print("Saved:", data)
        except Exception as e:
            print("Error saving:", e)

    def load_data(self) -> dict:
        path = self.get_save_path()
        try:
            if os.path.exists(path):
                with open(path, "r") as f:
                    data = json.load(f)
                print("Loaded:", data)
                return data
            else:
                print("No data found...")
        except Exception as e:
            print("Error loading:", e)
            return self.DEFAULT_SAVE.copy()

    def delete_save(self):
        path = self.get_save_path()
        print("Attempting to delete:", path)
        if os.path.exists(path):
            try:
                os.remove(path)
                print("Save file deleted.")
            except Exception as e:
                print("Failed to delete save:", e)
        else:
            print("No save file found to delete.")
