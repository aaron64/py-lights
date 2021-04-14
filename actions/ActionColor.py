from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *

###
# ActionColor: Displays a color
# Settings:
# 	Intensity - Intensity of the action
###
class ActionColor(Action):
	def __init__(self, params, name=None, color=WHITE, mask=None):
		super(ActionColor, self).__init__(params, name, "Color", False, mask)

		self.color = color

	def update(self, params):
		pass

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				addColorToStrip(strip, x, level_color(self.color, self.volume()))
	
