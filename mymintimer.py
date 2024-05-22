

class MinuteTimer:
	def __init__(self, minutes: int=1, target: int=0):
		self.last_trigger = 0
		self.minutes = minutes
		self.target = target

	def check_for_ding(self, now: int) -> bool:
		if ((now % (self.minutes*60)) == self.target):
			if (now > self.last_trigger):
				self.last_trigger = now
				return True
		return False
