import enum
from Timer import Timer

class TriggerStates(enum.Enum):
	Idle            = 1
	Attack          = 2
	Decay           = 4
	Sustain         = 8
	Release         = 16
	AttackCancelled = 32

class TriggerTypes(enum.Enum):
	Key     = 1
	Toggle  = 2
	Knob    = 4
	OneShot = 8

default_envelope = {
	"attack":  1,
	"decay":   1,
	"sustain": 1,
	"release": 1
}

class Trigger:
	def __init__(self, action, key, envelope=None, control="DEFAULT", type=TriggerTypes.Key, inverse=False):
		self.action = action
		self.key = key
		self.state = TriggerStates.Idle

		if envelope:
			self.envelope = {
				"attack":  envelope["attack"]  or 1,
				"decay":   envelope["decay"]   or 1,
				"sustain": envelope["sustain"] or 0,
				"release": envelope["release"] or 1
			}
		else:
			self.envelope = default_envelope

		self.control = control
		self.inverse = inverse

		self.attackTimer  = Timer(self.envelope["attack"])
		self.decayTimer   = Timer(self.envelope["decay"])
		self.releaseTimer = Timer(self.envelope["release"])

		self.val = 0

	def trigger(self, params, strip):
		self.state = TriggerStates.Attack
		self.attackTimer.reset()

		self.action.set(self.control, self.val, params)

	def keyUp(self, params):
		if self.state == TriggerStates.Attack:
			self.state = TriggerStates.AttackCancelled
			return
		self.state = TriggerStates.Release
		self.val = self.envelope['sustain']
		self.releaseTimer.reset()


	def update(self, params):
		if self.state == TriggerStates.Idle:
			return
		elif self.state == TriggerStates.Attack or self.state == TriggerStates.AttackCancelled:
			# interpolate from 0 to peak
			self.val = min(1, self.attackTimer.percent_finished())
			if self.attackTimer.expired():
				self.decayTimer.reset()
				self.releaseTimer.reset()
				self.state = TriggerStates.Decay if self.state == TriggerStates.Attack else TriggerStates.Release
		elif self.state == TriggerStates.Decay:
			# interpolate from attack level to sustain level
			self.val = 1-(self.decayTimer.percent_finished()*(1-self.envelope["sustain"]))
			if self.decayTimer.expired():
				self.state = TriggerStates.Sustain
		elif self.state == TriggerStates.Sustain:
			self.val = self.envelope["sustain"]
		elif self.state == TriggerStates.Release:
			self.val = self.envelope["sustain"]-(self.releaseTimer.percent_finished()*self.envelope["sustain"])
			self.val = max(0, self.val)
			if self.releaseTimer.expired():
				self.state = TriggerStates.Idle

		self.action.set(self.control, self.val, params)

	def mapVal(self, val):
		rangeVal = self.max - self.min
		return self.min + (float(val)/255) * rangeVal 