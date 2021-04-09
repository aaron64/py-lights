import time

class Timer:

	def __init__(self, duration=1):
		self.duration = duration
		self.expiration = self._current_millis() + duration

	def expired(self):
		return self.expiration <= self._current_millis()

	def percent_finished(self):
		return (self._current_millis() - (self.expiration-self.duration))/self.duration

	def reset(self):
		self.expiration = self._current_millis() + self.duration

	def soft_reset(self):
		pct_finished = min(self.percent_finished(), 1)
		self.expiration = self._current_millis() + self.duration * (1-pct_finished)

	def _current_millis(self):
		return time.time() * 1000