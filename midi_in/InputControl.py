
class InputControl:
	def __init__(self, action, type, key, setting, inverse=False, minVal=0, maxVal=255):
		self.action = action
		self.type = type
		self.inverse = inverse
		self.key = key
		self.setting = setting
		self.min = minVal
		self.max = maxVal

	def trigger(self, params, val):
		self.action.trigger(params, val)

    def triggerHold(self, params, val):
            if mapVal(val) != self.min:
                    self.action.trigger(params, mapVal(val))
            else:
                    self.action.release(params)

	def toggle(self, params):
		pass

	def hold(self, params, val):
		self.action.updateSetting(self.setting, mapVal(val))
	
	def knob(self, params, val):
		self.action.updateSetting(self.setting, mapVal(val))

	def mapVal(val):
		rangeVal = self.max - self.min
		return self.min + (float(val)/255) * rangeVal 
