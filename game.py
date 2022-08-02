import pygame
from sys import exit
from settings import *
from board import Board



class Game:

    def __init__(self) -> None:
        pygame.init()
        # Initializing game components
        self.board: list[list] = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.clock = pygame.time.Clock()

        # Game Information
        self.winner = None
        self.current_player: int = -1

        # Initializing and drawing window
        self.display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.game_board: Board = Board(self.board)
        self.display.fill(BLACK)
        self.game_board.draw()



    def __call__(self) -> None:
        self.run()


    def handle_turn(self, square) -> None:

        # Update game board
        row, col = square
        if self.board[row][col] != '-':
            print("Square is already a " + self.board[row][col])

        else:
            self.board[row][col] = "X" if self.current_player == -1 else "O"
            self.game_board.update(self.board)
            
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
                    square = self.game_board.get_square_from_pos(pos)
                    
                    self.handle_turn(square)
                    
                    print("Current player: ", "X" if self.current_player == -1 else "O")


            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == "X":
                        self.game_board.draw_x(j, i)
                    
                    elif self.board[i][j] == "O":
                        self.game_board.draw_o(j, i)
                    

    
            pygame.display.update()
            self.clock.tick(FPS)