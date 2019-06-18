from actions.Action import Action
from Color import Color

###
# ActionStrobe: Displays a color in a strobe pattern
# Settings:
# 	Intensity(0) - Intensity of the action
#	Speed(5) - Timeing of the strobe effect
###
class ActionStrobe(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionStrobe, self).__init__(params, "Strobe")
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 5
		self.parameters["Color"] = color

	def update(self, params):
		out = 0
		if (params["Counter"]/(self.settings["Speed"]+1))%2 == 1:
			out = self.settings["Intensity"]
		
		self.outputColor.r = int(self.parameters["Color"].r * (float(out)/255))
		self.outputColor.g = int(self.parameters["Color"].g * (float(out)/255))
		self.outputColor.b = int(self.parameters["Color"].b * (float(out)/255))
