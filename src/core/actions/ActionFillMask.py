from core.actions.Action import Action
from core.Setting import MAX_SPEED_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

###
# ActionFillMask: Fills the LEDs with a mask from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###


class ActionFillMask(Action):
    def __init__(self, name=None, mask=None):
        super(ActionFillMask, self).__init__(name, "Fill", False, mask)
        self.register_setting("Speed", MAX_SPEED_BOUNDS)
        self.register_setting("Position", MAX_POSITION_BOUNDS)

        self.timer = Timer()
        self.offset = 0

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Speed")

    def set(self, control, val):
        super().set(control, val)

    def trigger(self, app, velocity):
        self.offset = 0

    def render(self, strip):
        for x in self.mask:
            distance = abs(x - self.get("Position"))
            if distance < self.offset:
                mask_pixel(strip, x, 1-self.volume())
