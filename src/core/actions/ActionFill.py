from core.actions.Action import Action
from core.actions.Setting import MAX_SPEED_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

from core.entities.EntityFill import EntityFill

###
# ActionFill: Fills the LEDs from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionFill(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionFill, self).__init__(params, name, "Fill", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)
		self.register_setting("Position", MAX_POSITION_BOUNDS)

		self.color = color

	def trigger(self, app, params, velocity):
		app.add_entity(EntityFill(params, self.color, self.get("Speed"), self.get("Position")))