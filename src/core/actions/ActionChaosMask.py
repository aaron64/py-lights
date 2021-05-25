from core.actions.Action import Action
from core.actions.Setting import MAX_STROBE_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

import colorsys
import random

###
# ActionChaosMask: Masks a random strobe
# Settings:
# 	Intensity - Intensity of the action
# 	Speed	  - Time it takes for a color to reset
###
class ActionChaosMask(Action):
	def __init__(self, params, name=None, mask=None):
		super(ActionChaosMask, self).__init__(params, name, "Chaos Mask", False, mask)
		self.register_setting("Speed", MAX_STROBE_BOUNDS)

		self.buffer = []
		for i in range(params['LEDCount']):
			self.buffer.append({
				"timer": Timer(random.randint(self.get("Speed"), self.get("Speed")*2)),
				"on": random.choice([True, False])
			})

	def update(self, params):
		for buff in self.buffer:
			if buff["timer"].expired():
				buff["timer"].duration = random.randint(self.get("Speed"), self.get("Speed")*2)
				buff["timer"].reset()

				buff["on"] = not buff["on"]

	def render(self, params, strip):
		for x in self.mask:
			if self.buffer[x]["on"]:
				mask_pixel(strip, x, 1-self.volume())


