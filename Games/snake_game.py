import sys
import pygame
import random
from pygame.locals import *


# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game-云辉我们一起来玩吧！')

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_pos = [random.randrange(1, WINDOW_WIDTH//10) * 10, random.randrange(1, WINDOW_HEIGHT//10) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction

# Initialize game clock
clock = pygame.time.Clock()


# Game over function
def game_over():
    font = pygame.font.Font(None, 75)
    text = font.render('Game Over', True, RED)
    window.blit(text, [WINDOW_WIDTH // 2 - 135, WINDOW_HEIGHT // 2 - 50])
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                change_to = 'UP'
            if event.key == K_DOWN:
                change_to = 'DOWN'
            if event.key == K_LEFT:
                change_to = 'LEFT'
            if event.key == K_RIGHT:
                change_to = 'RIGHT'

    # Direction validation
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == fruit_pos:
        fruit_spawn = False
    else:
        snake_body.pop()

    # Fruit spawn
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, WINDOW_WIDTH//10) * 10, random.randrange(1, WINDOW_HEIGHT//10) * 10]
    fruit_spawn = True

    # Display update
    window.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, WHITE, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT-10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Refresh screen
    pygame.display.flip()

    speed = 5 + len(snake_body) / 2
    # Set game speed
    clock.tick(speed)

