
class InputControl:
	def __init__(self, _id, action, _type, key, setting, inverse=False, minVal=0, maxVal=255):
		self.id = _id
		self.action = action
		self.type = _type
		self.inverse = inverse
		self.key = key
		self.setting = setting
		self.min = minVal
		self.max = maxVal

	def trigger(self, params, val):
		self.action.trigger(params, self.mapVal(val))

	def triggerHold(self, params, val):
		if self.mapVal(val) != self.min:
			self.action.trigger(params, self.mapVal(val))
		else:
			self.action.release(params)

	def toggle(self, params):
		pass

	def hold(self, params, val):
		self.action.updateSetting(self.setting, self.mapVal(val))
	
	def knob(self, params, val):
		self.action.updateSetting(self.setting, self.mapVal(val))

	def mapVal(self, val):
		rangeVal = self.max - self.min
		return self.min + (float(val)/255) * rangeVal 
