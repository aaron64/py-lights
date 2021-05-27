from core.shapes.Shape import Shape
from core.Setting import MAX_VELOCITY_BOUNDS, MAX_WIDTH_BOUNDS

from core.context import context

from core.utils.Timer import Timer


class ShapeWave(Shape):
    def __init__(self, name):
        super(ShapeWave, self).__init__(name)

        self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)
        self.register_setting("Width", MAX_WIDTH_BOUNDS)

        self.set("Velocity", 0)
        self.set("Width", 0.2)

        self.timer = Timer()
        self.offset = 0

    def update(self):
        if self.timer.expired():
            self.timer.reset()
            self.offset += self.get("Velocity")

    def get_shape(self):
        shape = [0] * context.led_count
        for LED in range(context.led_count):
            level = (sin((x+self.offset)/self.get("Width"))+1)/2
            shape[LED] = level
            return shape
