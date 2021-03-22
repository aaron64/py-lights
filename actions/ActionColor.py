from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *

###
# ActionColor: Displays a color
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionColor(Action):
	def __init__(self, params, color = WHITE, mask="ALL"):
		super(ActionColor, self).__init__(params, False, mask)
		self.settings["Intensity"] = 0

		self.color = color

	def update(self, params):
		pass

	def render(self, params, strip):
		if self.settings["Intensity"] != 0:
			for x in self.mask:
				addColorToStrip(strip, x, level_color(self.color, self.settings["Intensity"]))
	
