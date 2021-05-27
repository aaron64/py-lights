from core.Setting import Setting
from core.utils.validation import validate_name


class Shape(object):
    def __init__(self, name):
        validate_name(name)

        self.name = name

        self.settings = {}
        self.action = None

    def update(self):
        pass

    def get_shape(self):
        pass

    def get(self, name):
        return self.settings[name].value

    def register_setting(self, name, bounds=None):
        setting = Setting(name, bounds)
        self.settings[name] = setting

    def get_settings(self):
        return self.settings
