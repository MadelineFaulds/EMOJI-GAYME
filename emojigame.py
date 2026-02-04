import pygame
import random 
import sys 

WINDOW_SIZE = 600 
GRID_SIZE = 6
CARD_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 30 

EMOJIS = ["😅","🚌","🥸","🪸","🙄","🍊","🐹","🤩","🫡","😜","😮","🌽","👙","🚤","🏝️","👛","🙈","🍓"]
random.shuffle(EMOJIS)

pygame.init() 
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Emoji Memory Game")
font = pygame.font.SysFont(None, 72)
clock = pygame.time.Clock()

cards = [{'emoji': EMOJIS[i], 'flipped': False, 'matched': False} for i in range(GRID_SIZE * GRID_SIZE)]
first_selection = None 


