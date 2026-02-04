import pygame
import random 
import sys 
import time 

WINDOW_SIZE = 600 
GRID_SIZE = 4
CARD_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 30 

EMOJIS = ["🥸","🥸","🪸","🪸","🍊","🍊","🐹","🐹","🤩","🤩","👙","👙","🙈","🙈","🍓","🍓"]
random.shuffle(EMOJIS)

pygame.init() 
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Emoji Memory Game")
font = pygame.font.SysFont("Apple Color Emoji", 7)
clock = pygame.time.Clock()

cards = [{'emoji': EMOJIS[i], 'flipped': False, 'matched': False} for i in range(GRID_SIZE * GRID_SIZE)]
first_selection = None 
def draw_board(): 
    for i, card in enumerate(cards): 
        x = (i % GRID_SIZE) * CARD_SIZE
        y = (i // GRID_SIZE) * CARD_SIZE
        rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
        pygame.draw.rect(screen, (200, 162, 200), rect)
        if card['flipped'] or card['matched']:
            emoji_surf = font.render(card['emoji'], True, (0, 0, 0))
            emoji_rect = emoji_surf.get_rect(center=rect.center)
            screen.blit(emoji_surf, emoji_rect)
        else:
            # Pink card color
            pygame.draw.rect(screen, (255, 182, 193), rect) 
            circle_radius = CARD_SIZE // 4
            pygame.draw.circle(screen, (255, 255, 255), rect.center, circle_radius)


def get_card_index(pos):
    x, y = pos
    col = x // CARD_SIZE
    row = y // CARD_SIZE
    return row * GRID_SIZE + col

first_selection = None
second_selection = None
flip_back_time = 0

running = True 
moves_left = 30  # Player starts with 30 moves
while running: 
    screen.fill((255, 255, 255))
    draw_board()
    # Display moves left
    moves_font = pygame.font.SysFont("Arial", 30)
    moves_text = moves_font.render(f"Moves Left: {moves_left}", True, (0, 0, 0))
    screen.blit(moves_text, (10, 10))
    pygame.display.flip()

    # Win or lose screen
    if all(card['matched'] for card in cards):
        win_font = pygame.font.SysFont("Arial", 60)
        win_text = win_font.render("You Win!", True, (0, 200, 0))
        win_rect = win_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
        screen.blit(win_text, win_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        continue
    elif moves_left <= 0:
        lose_font = pygame.font.SysFont("Arial", 60)
        lose_text = lose_font.render("Game Over!", True, (200, 0, 0))
        lose_rect = lose_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
        screen.blit(lose_text, lose_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
        continue
    clock.tick(FPS)


    if flip_back_time and pygame.time.get_ticks() >= flip_back_time:
        if first_selection is not None and second_selection is not None:
            # Only flip back if not matched
            if not cards[first_selection]['matched']:
                cards[first_selection]['flipped'] = False
            if not cards[second_selection]['matched']:
                cards[second_selection]['flipped'] = False
            first_selection = None
            second_selection = None
        flip_back_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Prevent flipping more than two cards at a time
            if second_selection is not None or flip_back_time:
                continue
            idx = get_card_index(event.pos)
            card = cards[idx]
            if not card['flipped'] and not card['matched']:
                card['flipped'] = True
                if first_selection is None:
                    first_selection = idx
                elif second_selection is None:
                    second_selection = idx
                    if cards[first_selection]['emoji'] == cards[second_selection]['emoji']:
                        cards[first_selection]['matched'] = True
                        cards[second_selection]['matched'] = True
                        first_selection = None
                        second_selection = None
                    else:
                        flip_back_time = pygame.time.get_ticks() + 1000
                        moves_left -= 1  # Decrement moves after two cards are flipped
pygame.quit() 
sys.exit() 
    






        