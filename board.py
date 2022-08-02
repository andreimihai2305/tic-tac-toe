import pygame
import math
from settings import *



class Board:

    def __init__(self, board) -> None:
        self.display = pygame.display.get_surface()
        self.board = board


    # Used to syncronize the visual board with game board
    def update(self, new_board) -> None:
        self.board = new_board


    def draw_x(self, x, y):
        pygame.draw.line(self.display, WHITE, (x * BOX_SIZE + 20, y * BOX_SIZE + 20), ((x + 1) * BOX_SIZE - 20, (y + 1) * BOX_SIZE - 20))
        pygame.draw.line(self.display, WHITE, ((x + 1) * BOX_SIZE - 20, y * BOX_SIZE + 20), (x * BOX_SIZE + 20, (y + 1) * BOX_SIZE - 20))


    def draw_o(self, x, y):
        pygame.draw.circle(self.display, WHITE, ((x * BOX_SIZE) + (BOX_SIZE // 2), (y * BOX_SIZE) + (BOX_SIZE // 2)), (BOX_SIZE // 2) - 20, 2)


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
        
