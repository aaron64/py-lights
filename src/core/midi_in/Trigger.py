import enum
from core.utils.Timer import Timer
from core.utils.hash_id import get_hash


class TriggerStates(enum.Enum):
    Idle = 1
    Attack = 2
    Decay = 4
    Sustain = 8
    Release = 16
    AttackCancelled = 32


class TriggerTypes(enum.Enum):
    Key = 1
    Toggle = 2
    Knob = 4
    OneShot = 8


DEFAULT_ENVELOPE = {
    "attack":  1,
    "decay":   1,
    "sustain": 1,
    "release": 1
}

DEFAULT_BOUNDS = (0, 1)


class Trigger:
    def __init__(self, action, key, control, value, envelope, bounds, type, only_while_on):
        self.id = get_hash()

        self.action = action
        self.key = key
        self.state = TriggerStates.Idle
        self.only_while_on = only_while_on
        self.value = value

        if envelope:
            self.envelope = {
                "attack":  envelope["attack"] or 1,
                "decay":   envelope["decay"] or 1,
                "sustain": envelope["sustain"] or 1,
                "release": envelope["release"] or 1
            }
        else:
            self.envelope = DEFAULT_ENVELOPE

        self.bounds = bounds

        self.type = type
        self.toggle = False

        self.control = control

        self.attack_timer = Timer(self.envelope["attack"])
        self.decay_timer = Timer(self.envelope["decay"])
        self.release_timer = Timer(self.envelope["release"])

        self.val = 0

    def trigger(self, app, velocity):
        if self.type == TriggerTypes.Toggle:
            if self.toggle:
                self.toggle = False
                self.action.set(self.control, self.bounds[0])
            else:
                self.toggle = True
                self.action.trigger(app, velocity)
                self.action.set(self.control, self.bounds[1])
            return

        if self.value is not None:
            self.action.set(self.control, self.value)
            return

        self.state = TriggerStates.Attack
        self.attack_timer.reset()

        self.action.trigger(app, velocity)
        self.action.set(self.control, self.val)

    def knob(self, velocity):
        minimum = self.bounds[0]
        maximum = self.bounds[1]
        diff = maximum - minimum
        val = velocity * diff + minimum

        if not self.only_while_on or self.action.is_on():
            self.action.set(self.control, val)

    def key_up(self):
        if self.state == TriggerStates.Attack:
            self.state = TriggerStates.AttackCancelled
            return
        self.state = TriggerStates.Release
        self.val = self.envelope['sustain']
        self.release_timer.reset()

    def update(self):
        if self.type == TriggerTypes.Key:
            self.update_key()
        else:
            return

        self.action.set(self.control, self.val)

    def update_key(self):
        if self.state == TriggerStates.Idle:
            return
        elif self.state == TriggerStates.Attack or self.state == TriggerStates.AttackCancelled:
            # interpolate from 0 to peak
            self.val = min(1, self.attack_timer.percent_finished())
            if self.attack_timer.expired():
                self.decay_timer.reset()
                self.release_timer.reset()
                self.state = TriggerStates.Decay if self.state == TriggerStates.Attack else TriggerStates.Release
        elif self.state == TriggerStates.Decay:
            # interpolate from attack level to sustain level
            self.val = 1-(self.decay_timer.percent_finished()
                          * (1-self.envelope["sustain"]))
            if self.decay_timer.expired():
                self.state = TriggerStates.Sustain
        elif self.state == TriggerStates.Sustain:
            self.val = self.envelope["sustain"]
        elif self.state == TriggerStates.Release:
            self.val = self.envelope["sustain"] - \
                (self.release_timer.percent_finished()
                 * self.envelope["sustain"])
            self.val = max(0, self.val)
            if self.release_timer.expired():
                self.val = 0
                self.action.release()
                self.state = TriggerStates.Idle

    def map_val(self, val):
        range_val = self.max - self.min
        return self.min + (float(val)/255) * range_val

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "key": self.key,
            "control": self.control,
            "envelope": self.envelope
        }
