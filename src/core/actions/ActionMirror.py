import enum
from core.actions.Action import Action
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *

from core.context import context

from math import floor

###
# ActionMirror: Displays a color
# Settings:
# 	Intensity - Intensity of the action
###


class MirrorDirection(enum.Enum):
    Left = 0
    Right = 1


class ActionMirror(Action):
    def __init__(self, name=None, mask=None):
        super(ActionMirror, self).__init__(name, "Mirror", False, mask)

    def update(self):
        pass

    def render_post(self, strip):
        for i in range(floor(LEDCount/2)):
            flip_index = LEDCount - i - 1

            color = strip.getPixelColor(i)
            set_color(strip, flip_index, color)
