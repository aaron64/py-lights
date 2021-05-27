from core.shapes.Shape import Shape
from core.Setting import MAX_STROBE_BOUNDS

from core.context import context

from core.utils.Timer import Timer


class ShapeStrobe(Shape):
    def __init__(self, name):
        super(ShapeStrobe, self).__init__(name)
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

    def get_shape(self):
        return [int(self.on)] * context.led_count
