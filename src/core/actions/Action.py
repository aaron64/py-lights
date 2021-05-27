from rpi_ws281x import Color
from core.Setting import Setting, DEFAULT_BOUNDS
from core.midi_in.Trigger import Trigger, TriggerTypes
from core.utils.hash_id import get_hash
from core.utils.validation import validate_name

from core.context import context

class Action(object):
    def __init__(self, name):
        validate_name(name)

        self.name = name
        self.id = get_hash()

        self.effects = {}
        self.shapes = {}

        self.settings = {}

        self.register_setting("Intensity")
        self.register_setting("Volume")

        self.set("Volume", 1)

        context.application.register_action(self)

    def effect(self, effect):
        if effect.name in self.effects:
            raise Exception(
                "Effect with name %s already registered" % effect.name)

        self.effects[effect.name] = effect
        effect.action = self

        for name, setting in effect.get_settings().items():
            self.add_setting(setting, '%s.%s' % (effect.name, setting.name))

        return self

    def shape(self, shape):
        if shape.name in self.shapes:
            raise Exception(
                "Shape with name %s already registered" % shape.name)

        self.shapes[shape.name] = shape
        shape.action = self

        for name, setting in shape.get_settings().items():
            self.add_setting(setting, '%s.%s' % (shape.name, setting.name))

        return self

    def bind_trigger(self, key, control="Intensity", value=None, envelope=None, bounds=DEFAULT_BOUNDS, type=TriggerTypes.Key, only_while_on=True):
        if not control in self.settings:
            raise Exception("Setting %s does not exist" % control)

        trigger = Trigger(self, key, control, value,
                          envelope, bounds, type, only_while_on)
        self.set(control, trigger.bounds[0])

        context.application.register_trigger(trigger)

        return self

    def knob(self, key, control="Intensity", value=None, envelope=None, bounds=DEFAULT_BOUNDS, only_while_on=True):
        return self.bind_trigger(key, control, value, envelope, bounds, TriggerTypes.Knob, only_while_on)

    def set(self, control, val):
        try:
            setting = self.settings[control]
            val = min(setting.bounds[1], val)
            val = max(setting.bounds[0], val)

            setting.value = val
        except Exception as e:
            print(e)

    def get(self, name):
        return self.settings[name].value

    def volume(self):
        return self.get("Intensity") * self.get("Volume")

    def is_on(self):
        return bool(self.volume())

    def update(self):
        if not self.is_on:
            return

        for name, shape in self.shapes.items():
            shape.update()
        for name, effect in self.effects.items():
            effect.update()

    def render(self, strip):
        if not self.is_on:
            return

        final_shape = [1] * context.led_count
        for name, shape in self.shapes.items():
            final_shape = [x * y for x,
                           y in zip(final_shape, shape.get_shape())]

        volume = self.volume()
        for name, effect in self.effects.items():
            effect.render(strip, volume, final_shape)

    def render_post(self, strip):
        if not self.is_on:
            return
        # TODO: we can speed this up...
        final_shape = [1] * context.led_count
        for name, shape in self.shapes.items():
            final_shape = [x * y for x,
                           y in zip(final_shape, shape.get_shape())]

        volume = self.volume()
        for name, effect in self.effects.items():
            effect.render_post(strip, volume, final_shape)
        pass

    def trigger(self, app, val):
        pass

    def release(self):
        pass

    def register_setting(self, name, bounds=None):
        setting = Setting(name, bounds)
        self.settings[name] = setting

    def add_setting(self, setting, name):
        self.settings[name] = setting

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "settings": list(map(Setting.to_dict, self.settings.values()))
        }
