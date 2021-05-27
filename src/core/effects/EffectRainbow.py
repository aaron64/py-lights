from core.effects.Effect import Effect
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.Setting import MAX_VELOCITY_BOUNDS

from core.context import context

import random
import colorsys


class EffectRainbow(Effect):
    def __init__(self, name):
        super(EffectRainbow, self).__init__(name)
        self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)

        self.timer = Timer()
        self.offset = 1

    def render(self, strip, volume, shape):
        for LED in range(context.led_count):
            (r, g, b) = colorsys.hsv_to_rgb((LED+self.offset)/count, 1.0, 1.0)
            color = Color(int(255 * r), int(255 * g), int(255 * b))

            add_color_to_strip(strip, LED, level_color(
                color, volume * shape[LED]))

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Velocity")
