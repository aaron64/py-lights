from core.entities.Entity import Entity
from core.colors import *
from core.utils.strip_utils import *

from core.utils.Timer import Timer

from math import floor

class EntityFill(Entity):
	def __init__(self, params, color=WHITE, speed=1, position=0):
		super(EntityFill, self).__init__(params)

		self.color = color

		self.position = position
		self.offset = 0
		self.speed = speed

		self.timer = Timer()

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.speed

			position_negative = self.position - self.offset
			position_positive = self.position + self.offset
			if position_negative < 0 and position_positive > params["LEDCount"]:
				self.finished = True


	def render(self, params, strip):
		for x in range(params["LEDCount"]):
			distance = abs(x - self.position)
			if distance < self.offset:
				add_color_to_strip(strip, x, self.color)
	
