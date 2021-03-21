
class Trigger:
	def __init__(envelope):
		self.envelope = {
			attack:  envelope.attack  or 0
			decay:   envelope.decay   or 0
			sustain: envelope.sustain or 0
			release: envelope.release or 0
		}