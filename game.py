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
        self.inner_table: list[list] = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.clock = pygame.time.Clock()
        self.board: Board = Board(self.inner_table)
        self.current_player: int = -1



    def __call__(self) -> None:
        self.run()


    def handle_turn(self, square) -> None:

        # Update game board
        row, col = square
        if self.inner_table[row][col] != '-':
            print("Square is already a " + self.inner_table[row][col])

        else:
            self.inner_table[row][col] = "X" if self.current_player == -1 else "O"
            self.board.update(self.inner_table)
            

            # Change player after turn end
            self.current_player *= -1
            
    




    def run(self) -> None:
        # Main game loop
        print("Current player: ", "X" if self.current_player == -1 else "O")
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    square = self.board.get_square_from_pos(pos)
                    
                    self.handle_turn(square)
                    
                    print("Current player: ", "X" if self.current_player == -1 else "O")


                    

            
            self.display.fill(BLACK)

            self.board.draw()
            
            pygame.display.update()
            self.clock.tick(FPS)