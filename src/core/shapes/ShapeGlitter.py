from core.shapes.Shape import Shape
from core.Setting import MAX_SPEED_BOUNDS

from core.context import context

from core.utils.Timer import Timer

from math import sin, pi
from random import randint, random


class ShapeGlitter(Shape):
    def __init__(self, name):
        super(ShapeGlitter, self).__init__(name)
        self.register_setting("Speed", MAX_SPEED_BOUNDS)
        self.settings["Speed"].value = 50

        self.buffer = []
        self.timers = []
        for i in range(context.led_count):
            timer = Timer(randint(
                self.get("Speed"), self.get("Speed")*2))
            self.timers.append(timer)
            self.buffer.append(randint(0, 1))

    def set(self, control, val):
        super().set(control, val)
        if control == "Speed":
            for LED in range(context.led_count):
                self.timers[LED].soft_reset()

    def update(self):
        for LED in range(context.led_count):
            if self.timers[LED].expired():
                self.timers[LED].duration = random(
                ) * self.get("Speed") + self.get("Speed")
                self.timers[LED].reset()
            self.buffer[LED] = 1-self.timers[LED].percent_finished()

    def get_shape(self):
        return self.buffer
