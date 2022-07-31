import pygame
from sys import exit
from settings import *

class Game():

	def __init__(self):
		pygame.init()

		# Initilizing display
		self.display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
		pygame.display.set_caption("Tic Tac Toe")

	# Calling the game
	def __call__(self) -> None:
		self.run()
		

	# Main Game loop
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
					


# Running the game
if __name__ == "__main__":
	tic_tac_toe = Game()
	tic_tac_toe()