from core.shapes.Shape import Shape
from core.Setting import MAX_STROBE_BOUNDS

from core.context import context


class ShapeMask(Shape):
    def __init__(self, name, mask=None):
        super(ShapeMask, self).__init__(name)

        self.mask = [1] * context.led_count
        if isinstance(mask, str):
            self.mask = [0] * context.led_count
            for LED in range(context.led_count):
                if eval(mask, {"x": LED}):
                    self.mask[LED] = 1
        else:
            self.mask = mask

    def get_shape(self):
        return self.mask
