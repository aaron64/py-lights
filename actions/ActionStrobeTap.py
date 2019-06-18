from actions.Action import Action
from Color import Color

###
# ActionStrobeTap: Displays a color in a strobe pattern to the beat of a tap
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionStrobeTap(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionStrobeTap, self).__init__(params, "Strobe Tap")
		self.settings["Intensity"] = 0
		self.parameters["Color"] = color

		self.rate = 0
		self.taps = 0
		self.countAtTap = 0

	def update(self, params):
		out = 0
		if (params["Counter"]/(self.rate+1))%2 == 1:
			out = self.settings["Intensity"]
		
		self.outputColor.r = int(self.parameters["Color"].r * (float(out)/255))
		self.outputColor.g = int(self.parameters["Color"].g * (float(out)/255))
		self.outputColor.b = int(self.parameters["Color"].b * (float(out)/255))

	def trigger(self, params, val):
		self.taps += 1
		if self.taps%2 == 0:
			self.rate = params["Counter"] - self.countAtTap
		else:
			self.countAtTap = params["Counter"]
