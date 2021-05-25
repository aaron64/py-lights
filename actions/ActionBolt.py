from actions.Action import Action
from actions.Setting import MAX_VELOCITY_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *

from entities.EntitySwipe import EntitySwipe

###
# ActionBolt: Displays a color
# Settings:
# 	Intensity - Intensity of the action
###
class ActionBolt(Action):
	def __init__(self, params, name=None, color=WHITE):
		super(ActionBolt, self).__init__(params, name, "Color", False)
		self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)
		self.register_setting("Position", MAX_POSITION_BOUNDS)

		self.color = color

	def trigger(self, app, params, val):
		app.add_entity(EntitySwipe(params, self.color, self.get("Velocity"), self.get("Position")))