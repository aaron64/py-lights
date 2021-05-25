from core.actions.Action import Action
from core.actions.Setting import MAX_VELOCITY_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

###
# ActionChaser: Displays a color that moves across in a loop
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionChaser(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionChaser, self).__init__(params, name, "Chaser", False, mask)
		self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)

		self.timer = Timer()
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Velocity")

	def set(self, control, val, params):
		super().set(control, val, params)

	def render(self, params, strip):
		for x in self.mask:
			add_color_to_strip(strip, (x+round(self.offset))%params['LEDCount'], level_color(self.color, self.volume()))
	
