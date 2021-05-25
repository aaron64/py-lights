from core.entities.Entity import Entity
from core.colors import *
from core.utils.strip_utils import *

from core.utils.Timer import Timer

from math import floor

class EntityBolt(Entity):
	def __init__(self, params, color=WHITE, velocity=1, position=0):
		super(EntityBolt, self).__init__(params)

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
	
