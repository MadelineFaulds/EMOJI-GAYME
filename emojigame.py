import pygame
import random 
import sys 

WINDOW_SIZE = 600 
GRID_SIZE = 6
CARD_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 30 

EMOJIS = ["😅","😅","🚌","🚌","🥸","🥸","🪸","🪸","🙄","🙄","🍊","🍊","🐹","🐹","🤩","🤩","🫡","🫡","😜","😜","😮","😮","🌽","🌽","👙","👙","🚤","🚤","🏝️","🏝️","👛","👛","🙈","🙈","🍓","🍓"]
random.shuffle(EMOJIS)

pygame.init() 
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Emoji Memory Game")
font = pygame.font.SysFont(None, 72)
clock = pygame.time.Clock()

cards = [{'emoji': EMOJIS[i], 'flipped': False, 'matched': False} for i in range(GRID_SIZE * GRID_SIZE)]
first_selection = None 

def draw_board(): 
    for i, card in enumerate(cards): 
        x = (i % GRID_SIZE) * CARD_SIZE
        y = (i // GRID_SIZE) * CARD_SIZE
        rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
        pygame.draw.rect (screen, (200, 200, 200), rect)
        pygame.draw.rect(screen, (100, 100, 100), rect, 2)
        if card['flipped'] or card['matched']:
            emoji_surf = font.render(card['emoji'], True, (0, 0, 0))
            emoji_rect = emoji_surf.get_rect(center=rect.center)
            screen.blit(emoji_surf, emoji_rect)
        else: 
            pygame.draw.rect(screen, (150, 150, 255), rect)

def get_card_index(pos):
    x, y = pos
    col = x // CARD_SIZE
    row = y // CARD_SIZE
    return row * GRID_SIZE + col

first_selection = None
second_selection = None
flip_back_time = 0

running = True 
while running: 
    screen.fill((255, 255, 255))
    draw_board()
    pygame.display.flip()
    clock.tick(FPS)


    if flip_back_time and pygame.time.get_ticks() >= flip_back_time:
        if first_selection is not None and second_selection is not None:
            cards [first_selection]['flipped'] = False
            cards [second_selection]['flipped'] = False
        first_selection = None
        second_selection = None
        flip_back_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            idx = get_card_index(event.pos)
            card = cards[idx] 
            if not card ['flipped'] and not card ['matched']: 
                card ['flipped'] = True 
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


pygame.quit() 
sys.exit() 
    




# main game loop
while running:
    screen.fill(PINK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if first_card is None or (first_card and second_card is None):
                for card in cards:
                    if card.rect.collidepoint(event.pos) and not card.revealed and not card.matched:
                        card.revealed = True
                        if first_card is None:
                            first_card = card
                        elif second_card:
                            second_card = card
                        break