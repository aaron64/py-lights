from core.effects.Effect import Effect
from core.Setting import MAX_STROBE_BOUNDS
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

from core.context import context

import colorsys
import random


class EffectChaos(Effect):
    def __init__(self, name, colors=None):
        super(EffectChaos, self).__init__(name)
        self.register_setting("Speed", MAX_STROBE_BOUNDS)

        self.colors = colors

        self.buffer = []
        for i in range(context.led_count):
            self.buffer.append({
                "timer": Timer(random.randint(round(self.get("Speed")), round(self.get("Speed")*2))),
                "color": self._get_next_color()
            })

    def set(self, control, val):
        super().set(control, val)
        if control == "Speed":
            for i in range(context.led_count):
                self.buffer[i]["timer"].soft_reset()

    def update(self):
        for buff in self.buffer:
            if buff["timer"].expired():
                buff["timer"].duration = random.randint(
                    round(self.get("Speed")), round(self.get("Speed")*2))
                buff["timer"].soft_reset()

                buff["color"] = self._get_next_color()

    def render(self, strip, volume, shape):
        for LED in range(context.led_count):
            add_color_to_strip(strip, LED, level_color(
                self.buffer[LED]["color"], volume * shape[LED]))


    def _get_next_color(self):
        if self.colors is None:
            x = random.uniform(0, 1)
            (r, g, b) = colorsys.hsv_to_rgb(x, 1.0, 1.0)
            color = Color(int(255 * r), int(255 * g), int(255 * b))
            return color
        else:
            return random.choice(self.colors)