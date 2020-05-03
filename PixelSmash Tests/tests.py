from TestAnimation import TestAnimation
from TestAnimator import TestAnimator

class Tests(object):
	
	def __init__(self):
		#self.testAnimation = TestAnimation()
		self.testAnimator = TestAnimator()

	def render(self, _screen):
		#self.testAnimation.render(_screen)
		self.testAnimator.render(_screen)

	def update(self, _dt):
		#self.testAnimation.update(_dt)
		self.testAnimator.update(_dt)