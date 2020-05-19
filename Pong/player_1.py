from paddle import Paddle


class Player_1(Paddle):
	def __init__(self):
		Paddle.__init__(self, "LEFT")