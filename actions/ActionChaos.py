from actions.Action import Action
from Color import Color

import random

###
# ActionChaos: Displays a strobe of random colors at random times
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionChaos(Action):
	def __init__(self, params):
		super(ActionChaos, self).__init__(params, "Chaos")
		self.settings["Intensity"] = 0

		self.counter = 0
		self.speed = 1

	def update(self, params):
		self.counter += 1

		if self.counter >= self.speed:
			self.counter = 0
			self.speed = random.randint(1, 7)
			self.color = Color.getRandomColor()

		
		self.outputColor.r = int(self.color.r * (float(self.settings["Intensity"])/255))
		self.outputColor.g = int(self.color.g * (float(self.settings["Intensity"])/255))
		self.outputColor.b = int(self.color.b * (float(self.settings["Intensity"])/255))
