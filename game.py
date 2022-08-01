import pygame
from sys import exit
from settings import *
from board import Board

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Initializing window
        self.display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")

        # Initializing game components
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_player = -1

        self.inner_table = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]


    def __call__(self) -> None:
        self.run()


    def handle_turn(self, square) -> None:

        # Update game board
        row, col = square
        if self.inner_table[row][col] != '-':
            print("Square is already a " + self.inner_table[row][col])

        else:
            self.inner_table[row][col] = "X" if self.current_player == -1 else "O"

            # Change player after turn end
            self.current_player *= -1
    
    

    def run(self) -> None:
        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("Current player: ", "X" if self.current_player == -1 else "O")
                    
                    pos = pygame.mouse.get_pos()
                    square = self.table.get_square_from_pos(pos)
                    
                    self.handle_turn(square)


                    

            self.display.fill(BLACK)

            self.board.draw()
            
            pygame.display.update()
            self.clock.tick(FPS)