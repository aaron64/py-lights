from core.actions.Action import Action
from core.Setting import MAX_STROBE_BOUNDS

from core.utils.strip_utils import *
from core.utils.Timer import Timer

###
# ActionMuteStrobe: Mutes the LEDs in a strobe pattern
# Settings:
# 	Mute  - Mutes the LEDs if value > 127
#	Speed - Timeing of the strobe effect
###


class ActionStrobeMask(Action):
    def __init__(self, name=None, mask=None):
        super(ActionStrobeMask, self).__init__(
            name, "Strobe Mask", False, mask)
        self.register_setting("Speed", MAX_STROBE_BOUNDS)
        self.on = False
        self.timer = Timer(self.get("Speed"))

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.on = not self.on

    def set(self, control, val):
        super().set(control, val)
        if control == "Speed":
            self.timer.duration = self.get("Speed")
            self.timer.soft_reset()

    def render_post(self, strip):
        if self.on:
            for x in self.mask:
                mask_pixel(strip, x, 1-self.volume())
