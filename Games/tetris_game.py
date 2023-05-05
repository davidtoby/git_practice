import sys
import pygame
import random
from pygame.locals import *


# 初始化 Pygame
pygame.init()

# 设置显示
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('俄罗斯方块')

# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [
    (0, 0, 0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218)
]

# 设置游戏变量
tetris_shapes = [
    [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']],
    [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']],
    [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']],
    [['.....',
      '.....',
      '.....',
      '0000.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..']],
    [['.....',
      '.....',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '.0...',
      '.00..',
      '.0...',
      '.....']],
    [['.....',
      '.....',
      '.0...',
      '.000.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '.0...',
      '.00..',
      '.0...',
      '.....']]
]


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]

    return grid


def valid_space(shape, grid):
    positions = shape.get_position()
    for pos in positions:
        if pos[1] > -1:
            if pos not in grid:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

"""
#def get_shape():
#   return Piece(random.randint(0, 7))
def get_shape():
    return Piece(5, 0, random.choice(tetris_shapes))
"""

def get_shape():
    return Piece(5, 0, random.choice(tetris_shapes))

def draw_window(surface, grid):
    surface.fill(BLACK)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (x * 30, y * 30, 30, 30
            ), 0)

    pygame.draw.rect(surface, (255, 255, 255), (10 * 30, 0, 30, WINDOW_HEIGHT), 5)
    pygame.display.update()


"""
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape.index(shape) + 1
        self.rotation = 0
"""

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = tetris_shapes.index(shape) + 1
        self.rotation = 0

    def get_position(self):
        positions = []
        shape_format = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(shape_format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((self.x + j, self.y + i))

        return positions

    def move(self, x, y):
        self.x += x
        self.y += y

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)


def main(window):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > 500:
            fall_time = 0
            current_piece.move(0, 1)
            if not valid_space(current_piece, grid):
                current_piece.move(0, -1)
                change_piece = True

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    current_piece.move(-1, 0)
                    if not valid_space(current_piece, grid):
                        current_piece.move(1, 0)
                if event.key == K_RIGHT:
                    current_piece.move(1, 0)
                    if not valid_space(current_piece, grid):
                        current_piece.move(-1, 0)
                if event.key == K_DOWN:
                    current_piece.move(0, 1)
                    if not valid_space(current_piece, grid):
                        current_piece.move(0, -1)
                if event.key == K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        current_piece.rotate(-1)

        if change_piece:
            for pos in current_piece.get_position():
                locked_positions[pos] = current_piece.color

            current_piece = get_shape()
            change_piece = False

            if check_lost(locked_positions):
                run = False

        draw_window(window, grid)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main(window)

