from entities.Entity import Entity
from colors import *
from strip_utils import *

from Timer import Timer

from math import floor

class EntitySwipe(Entity):
	def __init__(self, params, color=WHITE, velocity=1, position=0):
		super(EntitySwipe, self).__init__(params)

		self.color = color

		self.position = position
		self.velocity = velocity

		self.timer = Timer()

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.position += self.velocity
			if self.position < 0 or self.position > params["LEDCount"]:
				self.finished = True
			

	def render(self, params, strip):
		add_color_to_strip(strip, floor(self.position), self.color)
	
