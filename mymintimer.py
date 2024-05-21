

class MinuteTimer:
	def __init__(self, minutes: int=1):
		self.last_trigger = 0
		self.minutes = minutes

	def check_for_ding(self, now: int) -> bool:
		if ((now % (self.minutes*60)) == 0):
			if (now > self.last_trigger):
				self.last_trigger = now
				return True
		return False
