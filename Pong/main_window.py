from pixelsmash.main_window import PSMainWindow

from states_manager import StatesManager
from settings import SWIDTH, SHEIGHT, WCAPTION

if __name__ == "__main__":
	PSMainWindow(SWIDTH, SHEIGHT, WCAPTION, StatesManager()) 