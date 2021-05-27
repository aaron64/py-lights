from core.actions.Action import Action
from core.Setting import MAX_SPEED_BOUNDS, MAX_POSITION_BOUNDS, MAX_SPACING_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

###
# ActionRings: Fills the LEDs from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###


class ActionRings(Action):
    def __init__(self, name=None, color=WHITE, mask=None):
        super(ActionRings, self).__init__(name, "Fill", False, mask)
        self.register_setting("Speed", MAX_SPEED_BOUNDS)
        self.register_setting("Position", MAX_POSITION_BOUNDS)
        self.register_setting("Spacing", MAX_SPACING_BOUNDS)

        self.set("Speed", 1)

        self.timer = Timer()
        self.offset = 0

        self.color = color

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Speed")

    def trigger(self, app, velocity):
        self.offset = 0

    def render(self, strip):
        for x in self.mask:
            distance = abs(x - self.get("Position"))
            if distance < self.offset:
                add_color_to_strip(strip, x, level_color(
                    self.color, self.volume()))
