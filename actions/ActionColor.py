from actions.Action import Action
from Color import Color

###
# ActionColor: Displays a color
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionColor(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionColor, self).__init__(params, "Color")
		self.settings["Intensity"] = 0
		self.color = color

	def update(self, params):
		self.outputColor.r = int(self.color.r * (float(self.settings["Intensity"])/255))
		self.outputColor.g = int(self.color.g * (float(self.settings["Intensity"])/255))
		self.outputColor.b = int(self.color.b * (float(self.settings["Intensity"])/255))
	
		
