from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *

###
# ActionChaser: Displays a color that moves across in a loop
# Settings:
# 	Intensity(0) - Intensity of the action
# 	Velocity - Speed and direction of flow
###
class ActionChaser(Action):
	def __init__(self, params, color = WHITE, mask="ALL"):
		super(ActionChaser, self).__init__(params, False, mask)
		self.settings["Intensity"] = 0
		self.settings["Velocity"] = 0.1
		self.offset = 0

		self.color = color

	def update(self, params):
		self.offset += self.settings["Velocity"]

	def render(self, params, strip):
		if self.settings["Intensity"] != 0:
			for x in self.mask:
				addColorToStrip(strip, (x+round(self.offset))%params['LEDCount'], level_color(self.color, self.settings["Intensity"]))
	
