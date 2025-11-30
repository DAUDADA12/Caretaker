import json
import os
from py4godot.classes.Node2D import Node2D
from py4godot.classes import gdclass

@gdclass
class Data_Puller(Node2D):

	SAVE_PATH = "save_data.json"

	DEFAULT_SAVE = {
		'petName':'',
		'petAge' : 0,
		'petHunger' : 100,
		'petEnergy' : 100,
		'petType' : 0
	}

	def _ready(self):
		print("SaveManager ready!")
		data = self.load_data()
		print("Loaded:", data)

	def save_data(self, data: dict):
		try:
			with open(self.get_save_path(), "w") as f:
				json.dump(data, f, indent=4)
			print("Saved:", data)
		except Exception as e:
			print("Error saving:", e)

	def load_data(self) -> dict:
		try:
			path = self.get_save_path()

			if os.path.exists(path):
				with open(path, "r") as f:
					return json.load(f)
			else:
				print("No save file found → creating new save...")
				self.save_data(self.DEFAULT_SAVE)
				return self.DEFAULT_SAVE.copy()

		except Exception as e:
			print("Error loading:", e)
			return self.DEFAULT_SAVE.copy()

	def get_save_path(self) -> str:
		base = os.getcwd()
		return os.path.join(base, self.SAVE_PATH)