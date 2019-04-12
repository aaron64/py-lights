import os

class InputLogger():
	def __init__(self):
		self.inputs = []

	def addInput(self, midiInput):
		self.inputs.append(midiInput)

	def print(self):
		os.system("cls" if os.nam=="nt" else "clear")
