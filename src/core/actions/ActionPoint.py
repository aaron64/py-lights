from core.actions.Action import Action
from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.Setting import MAX_POSITION_BOUNDS, MAX_WIDTH_BOUNDS

###
# ActionPoint: Displays a color
# Settings:
# 	Intensity - Intensity of the action
###


class ActionPoint(Action):
    def __init__(self, name=None, color=WHITE, mask=None):
        super(ActionPoint, self).__init__(name, "Color", False, mask)

        self.register_setting("Position", MAX_POSITION_BOUNDS)
        self.register_setting("Width", MAX_WIDTH_BOUNDS)

        self.color = color

    def update(self):
        pass

    def render(self, strip):
        for x in self.mask:
            dist = abs(self.get("Position") - x)
            if(dist < self.get("Width")):
                add_color_to_strip(strip, x, level_color(
                    self.color, self.volume()))
