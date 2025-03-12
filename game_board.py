import numpy as np
import pygame

def create_board():
    return np.full((3, 3), ' ')  # Creates a 3x3 board filled with spaces

def draw_board(screen):
    screen.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 5)

def draw_figures(screen, board):
    for row in range(3):
        for col in range(3):
            if board[row, col] == 'X':
                pygame.draw.line(screen, (200, 0, 0), (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), 5)
                pygame.draw.line(screen, (200, 0, 0), (col * 200 + 150, row * 200 + 50), (col * 200 + 50, row * 200 + 150), 5)
            elif board[row, col] == 'O':
                pygame.draw.circle(screen, (0, 0, 200), (col * 200 + 100, row * 200 + 100), 50, 5)

def check_winner(board):
    for player in ['X', 'O']:
        for i in range(3):
            if all(board[i, :] == player) or all(board[:, i] == player):
                return player
        if board[0, 0] == board[1, 1] == board[2, 2] == player or board[0, 2] == board[1, 1] == board[2, 0] == player:
            return player
    return None if ' ' in board else 'Draw'

def restart_game(board):
    board.fill(' ')
