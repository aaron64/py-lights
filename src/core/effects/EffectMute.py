from core.effects.Effect import Effect
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

from core.context import context


class EffectMute(Effect):
    def __init__(self, name):
        super(EffectMute, self).__init__(name)

    def update(self):
        pass

    def render_post(self, strip, volume, shape):
        for LED in range(context.led_count):
            mask_pixel(strip, LED, 1 - volume * shape[LED])
