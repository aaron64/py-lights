from core.shapes.Shape import Shape
from core.Setting import MAX_STROBE_BOUNDS
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

from core.context import context

import colorsys
import random


class ShapeChaos(Shape):
    def __init__(self, name, colors=None):
        super(ShapeChaos, self).__init__(name)
        self.register_setting("Speed", MAX_STROBE_BOUNDS)
        self.register_setting("Threshold")

        self.settings["Speed"].value = 100
        self.settings["Threshold"].value = 0.5

        self.colors = colors

        self.buffer = []
        self.timers = []
        for i in range(context.led_count):
            self.buffer.append(random.randint(0, 1))
            self.timers.append(Timer(random.randint(round(self.get("Speed")), round(self.get("Speed")*2))))

    def set(self, control, val):
        super().set(control, val)
        if control == "Speed":
            for LED in range(context.led_count):
                self.timers[LED].soft_reset()

    def update(self):
        for LED in range(context.led_count):
            if self.timers[LED].expired():
                self.timers[LED].duration = random.randint(
                    round(self.get("Speed")), round(self.get("Speed")*2))
                self.timers[LED].reset()

            self.buffer[LED] = (int)(self.timers[LED].percent_finished() > self.get("Threshold"))

    def get_shape(self):
        return self.buffer
