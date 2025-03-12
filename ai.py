import numpy as np
import random
from game_board import check_winner

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == ' ':
                board[i, j] = 'O'
                score = minimax(board, False)  # Make sure minimax is defined
                board[i, j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move] = 'O'

# Easy AI: Makes random moves
def random_ai(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r, c] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row, col] = 'O'

# Medium AI: Learns over time (Progressive AI)
ai_memory = {}

def progressive_ai(board):
    if random.random() < 0.3:  # 30% chance AI makes a random move
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r, c] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            board[row, col] = 'O'
            print("Progressive AI made a random move.")
            return

    print("Progressive AI calling ai_move()...")  # Debugging print
    ai_move(board)  # Calls ai_move to play optimally
    print("Progressive AI executed ai_move() successfully.")  # Debugging print

    ai_memory[str(board)] = True  # AI remembers movess

# Hard AI: Unbeatable using Minimax
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return -1
    if winner == 'O': return 1
    if np.all(board != ' '): return 0  # Draw

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == ' ':
                    board[i, j] = 'O'
                    score = minimax(board, False)
                    board[i, j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == ' ':
                    board[i, j] = 'X'
                    score = minimax(board, True)
                    board[i, j] = ' '
                    best_score = min(best_score, score)
        return best_score

def unbeatable_ai(board):
    best_score = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == ' ':
                board[i, j] = 'O'
                score = minimax(board, False)
                board[i, j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move] = 'O'
