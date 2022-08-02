import pygame
from sys import exit
from settings import *
from board import Board



class Game:

    def __init__(self) -> None:
        pygame.init()
        # Initializing game components
        self.clock = pygame.time.Clock()
        self.board: list[list] = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

        # Game Information
        self.winner = None
        self.current_player: int = -1

        # Initializing and drawing window
        self.display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.game_board: Board = Board(self.board)
        self.display.fill(BLACK)
        self.game_board.draw_game_board()



    def __call__(self) -> None:
        self.run()


    def handle_turn(self, square) -> None:

        
        row, col = square
        if self.board[row][col] != '-':
            print("Square is already a " + self.board[row][col])

        else:
            # Update game board
            self.board[row][col] = "X" if self.current_player == -1 else "O"
            
            # Update visual board
            self.game_board.update(self.board)
            
            # Change player after turn end
            self.current_player *= -1


    def check_if_game_ended(self) -> None:
        for i in range(len(self.board)):
            # Check for horizontal winner
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '-':
                self.winner = "X" if self.board[i][0] == "X" else "O"
                self.game_board.draw_win_line_horizontal(i)
                print("Winner: " + self.winner)
                break

            # Check for vertical winner
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '-':
                self.winner = "X" if self.board[0][i] == "X" else "O"
                self.game_board.draw_win_line_vertical(i)
                print("Winner: " + self.winner)
                break

        # Check for diagonal winner
        else:
            if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != '-':
                self.winner = "X" if self.board[1][1] == "X" else "O"
                self.game_board.draw_win_line_diagonal(-1)
                print("Winner: " + self.winner)

            if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != '-':
                self.winner = "X" if self.board[1][1] == "X" else "O"
                self.game_board.draw_win_line_diagonal(1)
                print("Winner: " + self.winner)


    def run(self) -> None:
        # Main game loop
        print("Current player: ", "X" if self.current_player == -1 else "O")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.winner:
                        pos = pygame.mouse.get_pos()
                        square = self.game_board.get_square_from_pos(pos)
                        
                        self.handle_turn(square)
                        print("Current player: ", "X" if self.current_player == -1 else "O")
                        self.check_if_game_ended()


            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == "X":
                        self.game_board.draw_x(j, i)
                    
                    elif self.board[i][j] == "O":
                        self.game_board.draw_o(j, i)
                    

            self.clock.tick(FPS)
            pygame.display.flip()