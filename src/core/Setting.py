from core.utils.validation import validate_name

MAX_SPEED_BOUNDS = (1, 50000)
MAX_POSITION_BOUNDS = (-1024, 1024)
MAX_VELOCITY_BOUNDS = (-1024, 1024)
MAX_STROBE_BOUNDS = (25, 5000)
MAX_WIDTH_BOUNDS = (0.01, 10)
MAX_SPACING_BOUNDS = (1, 512)

DEFAULT_BOUNDS = (0, 1)


class Setting(object):
    def __init__(self, name, bounds=None):
        validate_name(name)

        self.name = name

        if bounds is None:
            bounds = DEFAULT_BOUNDS
        self.bounds = bounds

        self.value = bounds[0]

    def to_dict(self):
        return {
            "name": self.name,
            "bounds": self.bounds,
            "value": self.value
        }
