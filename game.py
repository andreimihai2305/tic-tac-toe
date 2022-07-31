import pygame
from sys import exit
from settings import *
from table import Table

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Initializing window
        self.display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")

        self.clock = pygame.time.Clock()

        # Initializing game components
        self.table = Table()

    
    def __call__(self) -> None:
        self.run()
    
    def run(self):
        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display.fill(BLACK)

            self.table.draw()
            
            pygame.display.update()
            self.clock.tick(FPS)