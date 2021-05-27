from core.shapes.Shape import Shape
from core.Setting import MAX_VELOCITY_BOUNDS

from core.context import context

from core.utils.Timer import Timer


class ShapeChaser(Shape):
    def __init__(self, name):
        super(ShapeChaser, self).__init__(name)
        self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)

        self.timer = Timer()
        self.offset = 0

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Velocity")

    def get_shape(self):
        shape = [0] * context.led_count

        pos = round(self.offset) % context.led_count
        shape[pos] = 1
        return shape
