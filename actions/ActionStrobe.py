from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *

###
# ActionStrobe: Displays a color in a strobe pattern
# Settings:
# 	Intensity(0) - Intensity of the action
#	Speed(5) - Timeing of the strobe effect
###
class ActionStrobe(Action):
	def __init__(self, params, color = WHITE):
		super(ActionStrobe, self).__init__(params)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 1
		self.on = False
		self.color = color
		self.nextFlip = params['Counter'] + self.settings["Speed"]

	def set(self, control, val, params):
		if control == "INTENSITY":
			self.settings["Intensity"] = val

	def update(self, params):
		if params['Counter'] > self.nextFlip:
			self.nextFlip = params['Counter'] + self.settings["Speed"]			
			self.on = not self.on

	def render(self, params, strip):
		if self.on:
			for x in range(0, params['LEDCount']):
				addColorToStrip(strip, x, level_color(self.color, self.settings["Intensity"]))