from actions.Action import Action

from Color import Color

class ActionStrobe(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionStrobe, self).__init__(params)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 5

		self.counter = 0
		self.state = True

		self.color = color

	def update(self, params):
		self.counter += 1

		if self.counter >= self.settings["Speed"]:
			self.counter = 0
			self.state = not self.state

		out = 0
		if (params["Counter"]/(self.settings["Speed"]+1))%2 == 1:
			out = self.settings["Intensity"]
		
		self.settings["Color"].r = int(self.color.r * (float(out)/255))
		self.settings["Color"].g = int(self.color.g * (float(out)/255))
		self.settings["Color"].b = int(self.color.b * (float(out)/255))
