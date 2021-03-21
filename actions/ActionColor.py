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
	def __init__(self, params, color = WHITE, keys="ALL"):
		super(ActionColor, self).__init__(params)
		self.settings["Intensity"] = 0
		if keys == "ALL":
			self.keys = [*range(params["LEDCount"])]
		else:
			self.keys = keys

		self.color = color

	def set(self, control, val, params):
		if control == "INTENSITY":
			print(val)
			self.settings["Intensity"] = val

	def update(self, params):
		pass

	def render(self, params, strip):
		for x in self.keys:
			addColorToStrip(strip, x, level_color(self.color, self.settings["Intensity"]))
	
		
