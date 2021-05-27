from core.actions.Action import Action
from core.Setting import MAX_VELOCITY_BOUNDS, MAX_WIDTH_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

from math import sin, pi

###
# ActionNoise: Displays 1D perlin noise
# Settings:
# 	Intensity - Intensity of the action
# 	Width - Size of the noise
###


class ActionNoise(Action):
    def __init__(self, name=None, color=WHITE, mask=None):
        super(ActionNoise, self).__init__(name, "Noise", False, mask)
        self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)
        self.register_setting("Width", MAX_WIDTH_BOUNDS)

        self.timer = Timer()
        self.offset = 0

        self.color = color

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Velocity")

    def render(self, strip):
        for x in self.mask:
            pos = x + self.offset
            val = sin(self.get("Width") * pos) + sin(pi * pos)+1
            val *= 0.5
            add_color_to_strip(strip, x, level_color(
                self.color, val * self.volume()))
