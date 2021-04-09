from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

###
# ActionFill: Fills the LEDs from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionFill(Action):
	def __init__(self, params, color = WHITE, mask=None):
		super(ActionFill, self).__init__(params, False, mask)
		self.settings["Speed"] = 10
		self.settings["Position"] = params["LEDCount"]/2

		self.timer = Timer(60)
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.settings["Speed"]

	def set(self, control, val, params):
		super().set(control, val, params)

	def trigger(self, params, velocity):
		self.offset = 0

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				distance = abs(x - self.settings["Position"])
				if distance < self.offset:
					addColorToStrip(strip, x, level_color(self.color, self.volume()))
	
