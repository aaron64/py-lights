from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

###
# ActionChaser: Displays a color that moves across in a loop
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionChaser(Action):
	def __init__(self, params, color = WHITE, mask=None):
		super(ActionChaser, self).__init__(params, False, mask)
		self.settings["Velocity"] = 0.1

		self.timer = Timer(60)
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.settings["Velocity"]

	def set(self, control, val, params):
		super().set(control, val, params)

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				addColorToStrip(strip, (x+round(self.offset))%params['LEDCount'], level_color(self.color, self.volume()))
	
