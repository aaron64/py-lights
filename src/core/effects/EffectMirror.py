from core.effects.Effect import Effect
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

from core.context import context

from math import floor

class EffectMirror(Effect):
    def __init__(self, name):
        super(EffectMirror, self).__init__(name)

    def update(self):
        pass

    def render_post(self, strip, volume, shape):
        for LED in range(floor(context.led_count/2)):
            flip_index = context.led_count - LED - 1

            color = strip.getPixelColor(LED)
            set_color(strip, flip_index, color)
