import pygame
from game_board import create_board, draw_board, draw_figures, check_winner, restart_game
from player import player_move
from ai import random_ai, progressive_ai, unbeatable_ai

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")
font = pygame.font.Font(None, 40)

# Game Variables
board = create_board()
player_turn = True
difficulty = None  # Stores the selected difficulty


def show_menu():
    global difficulty
    screen.fill((255, 255, 255))

    title_text = font.render("Choose AI Difficulty", True, (0, 0, 0))
    easy_text = font.render("1 - Easy (Random AI)", True, (0, 0, 255))
    medium_text = font.render("2 - Medium (Progressive AI)", True, (255, 165, 0))
    hard_text = font.render("3 - Hard (Unbeatable AI)", True, (255, 0, 0))

    screen.blit(title_text, (WIDTH // 4, HEIGHT // 4))
    screen.blit(easy_text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(medium_text, (WIDTH // 4, HEIGHT // 2.5))
    screen.blit(hard_text, (WIDTH // 4, HEIGHT // 2.1))

    pygame.display.update()

    selecting = True
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                    selecting = False
                elif event.key == pygame.K_2:
                    difficulty = "medium"
                    selecting = False
                elif event.key == pygame.K_3:
                    difficulty = "hard"
                    selecting = False

    screen.fill((255, 255, 255))
    draw_board(screen)
    pygame.display.update()


# Start Menu
show_menu()

# Game loop
running = True
while running:
    draw_board(screen)
    draw_figures(screen, board)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            row, col = player_move(event.pos, board)
            if row is not None:
                player_turn = False  # Switch to AI

    if not player_turn:
        pygame.time.delay(500)  # AI delay for realism

        if difficulty == "easy":
            random_ai(board)
        elif difficulty == "medium":
            progressive_ai(board)
        elif difficulty == "hard":
            unbeatable_ai(board)

        player_turn = True

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!" if winner != 'Draw' else "It's a draw!")
        pygame.time.delay(2000)
        restart_game(board)
