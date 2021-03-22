import enum

class TriggerStates(enum.Enum):
	Idle            = 1
	Attack          = 2
	Decay           = 4
	Sustain         = 8
	Release         = 16
	AttackCancelled = 32

default_envelope = {
	"attack":  1,
	"decay":   1,
	"sustain": 1,
	"release": 1	
}

class Trigger:
	def __init__(self, action, key, envelope=None, control="DEFAULT", oneShot=False, toggle=False, inverse=False, minVal=0, maxVal=255):
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
		self.oneShot = oneShot
		self.toggle  = toggle

		self.inverse = inverse
		self.min = minVal
		self.max = maxVal

		self.triggerTime = 0

		self.val = 0

	def trigger(self, params, strip):
		self.triggerTime = params['Counter']
		self.state = TriggerStates.Attack

		self.action.set(self.control, self.val, params)

	def keyUp(self, params):
		if self.oneShot or self.toggle:
			print("Oneshot or toggle, skipping")
			return
		if self.state == TriggerStates.Attack:
			self.state = TriggerStates.AttackCancelled
			return
		self.triggerTime = params['Counter']
		self.val = self.envelope['sustain']
		self.state = TriggerStates.Release


	def update(self, params):
		# print("----------------")
		duration = params['Counter'] - self.triggerTime
		# print("duration %s" % duration)
		if self.state == TriggerStates.Idle:
			return
		elif self.state == TriggerStates.Attack or self.state == TriggerStates.AttackCancelled:
			# interpolate from 0 to peak
			# print("attack")
			self.val = min(1, duration / self.envelope["attack"])
			if duration >= self.envelope["attack"]:
				self.triggerTime = params["Counter"]
				self.state = TriggerStates.Decay if self.state == TriggerStates.Attack else TriggerStates.Release
		elif self.state == TriggerStates.Decay:
			# interpolate from attack level to sustain level
			# print("decay")
			self.val = 1-((1 - self.envelope["sustain"]) * (duration/self.envelope["decay"]))
			if duration >= self.envelope["decay"]:
				self.triggerTime = params["Counter"]
				self.state = TriggerStates.Sustain
		elif self.state == TriggerStates.Sustain:
			# print("sustain")
			self.val = self.envelope["sustain"]
		elif self.state == TriggerStates.Release:
			# print("release")
			self.val = (1 - (duration/self.envelope["release"])) * self.envelope["sustain"]
			self.val = max(0, self.val)
			if duration >= self.envelope["release"]:
				self.state = TriggerStates.Idle
		# print("val %s" % self.val)
		self.action.set(self.control, self.val, params)

	# def triggerHold(self, params, val):
	# 	if self.mapVal(val) != self.min:
	# 			self.action.trigger(params, self.mapVal(val))
	# 	else:
	# 			self.action.release(params)

	# def toggle(self, params):
	# 	pass

	# def hold(self, params, val):
	# 	self.action.updateSetting(self.setting, self.mapVal(val))
	
	# def knob(self, params, val):
	# 	self.action.updateSetting(self.setting, self.mapVal(val))

	def mapVal(self, val):
		rangeVal = self.max - self.min
		return self.min + (float(val)/255) * rangeVal 
