from core.actions.Action import Action
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

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
		for x in self.mask:
			add_color_to_strip(strip, x, level_color(self.color, self.volume()))
	
