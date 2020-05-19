from paddle import Paddle


class Player_2(Paddle):
	def __init__(self):
		Paddle.__init__(self, "RIGHT")