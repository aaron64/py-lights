from core.effects.Effect import Effect
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

from core.context import context


class EffectColor(Effect):
    def __init__(self, name, color=WHITE):
        super(EffectColor, self).__init__(name)

        self.color = color

    def update(self):
        pass

    def render(self, strip, volume, shape):
        for LED in range(context.led_count):
            add_color_to_strip(strip, LED, level_color(
                self.color, volume * shape[LED]))
