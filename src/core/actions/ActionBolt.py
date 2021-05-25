from core.actions.Action import Action
from core.actions.Setting import MAX_VELOCITY_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

from core.entities.EntityBolt import EntityBolt

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
		app.add_entity(EntityBolt(params, self.color, self.get("Velocity"), self.get("Position")))