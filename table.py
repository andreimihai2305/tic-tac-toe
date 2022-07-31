import pygame
from settings import *

class Table:

    def __init__(self) -> None:
        self.display = pygame.display.get_surface()
        pass

    def draw(self):
        # Drawing vertical Lines
        pygame.draw.line(self.display, WHITE, (BOX_SIZE, 0), (BOX_SIZE, SCREEN_SIZE))
        pygame.draw.line(self.display, WHITE, (BOX_SIZE * 2, 0), (BOX_SIZE * 2, SCREEN_SIZE))

        # Drawing horizontal lines
        pygame.draw.line(self.display, WHITE, (0, BOX_SIZE), (SCREEN_SIZE, BOX_SIZE)) 
        pygame.draw.line(self.display, WHITE, (0, BOX_SIZE * 2), (SCREEN_SIZE, BOX_SIZE * 2)) 
        
