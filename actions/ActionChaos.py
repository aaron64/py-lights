from actions.Action import Action

from Color import Color

import random

class ActionChaos(Action):
	def __init__(self, params):
		super(ActionChaos, self).__init__(params)
		self.settings["Intensity"] = 0

		self.counter = 0
		self.speed = 1
		self.color = color

	def update(self, params):
		self.counter += 1

		if self.counter >= self.speed:
			self.counter = 0
			self.speed = random.randint(1, 7)
			self.color = Color.getRandomColor()

		out = 0
		if (params["Counter"]/(self.settings["Speed"]+1))%2 == 1:
			out = self.settings["Intensity"]
		
		self.settings["Color"].r = int(self.color.r * (float(out)/255))
		self.settings["Color"].g = int(self.color.g * (float(out)/255))
		self.settings["Color"].b = int(self.color.b * (float(out)/255))
