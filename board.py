import pygame, math
from settings import *

class Board:

    def __init__(self) -> None:
        self.display = pygame.display.get_surface()
        pass

    def draw(self) -> None:
        # Drawing vertical Lines
        pygame.draw.line(self.display, WHITE, (BOX_SIZE, 0), (BOX_SIZE, SCREEN_SIZE))
        pygame.draw.line(self.display, WHITE, (BOX_SIZE * 2, 0), (BOX_SIZE * 2, SCREEN_SIZE))

        # Drawing horizontal lines
        pygame.draw.line(self.display, WHITE, (0, BOX_SIZE), (SCREEN_SIZE, BOX_SIZE)) 
        pygame.draw.line(self.display, WHITE, (0, BOX_SIZE * 2), (SCREEN_SIZE, BOX_SIZE * 2)) 


    def get_square_from_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        x, y = pos

        row = (y + BOX_SIZE) / BOX_SIZE
        row = math.floor(row)

        column = (x + BOX_SIZE) / BOX_SIZE
        column = math.floor(column)

        return (row - 1, column - 1)
        
