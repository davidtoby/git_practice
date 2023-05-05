import sys
import pygame
import random
import itertools

# 初始化 Pygame
pygame.init()
pygame.key.set_repeat(200, 50)

# 定义常量
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)

shapes = [
    [
        "1110",
        "0100",
        "0000",
    ],
    [
        "0110",
        "1100",
        "0000",
    ],
    [
        "0100",
        "1110",
        "0000",
    ],
    [
        "1100",
        "0110",
        "0000",
    ],
    [
        "1111",
        "0000",
    ],
    [
        "1100",
        "1100",
    ],
]

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

# 创建方块
def create_block():
    shape = random.choice(shapes)
    color = random.choice(colors)
    return {
        "shape": shape,
        "color": color,
        "position": [GRID_WIDTH // 2, 0],
        "rotation": 0,
    }

# 绘制方块
def draw_block(screen, block):
    shape = block["shape"]
    color = block["color"]
    position = block["position"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell == "1":
                rect = pygame.Rect(
                    (position[0] + x) * GRID_SIZE,
                    (position[1] + y) * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE,
                )
                pygame.draw.rect(screen, color, rect, 0)

# 主循环
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    clock = pygame.time.Clock()
    current_block = create_block()
    grid = [["" for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_block(screen, current_block)
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, SCREEN_WIDTH, GRID_SIZE), 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block["position"][0] -= 1
                elif event.key == pygame.K_RIGHT:
                    current_block["position"][0] += 1
                elif event.key == pygame.K_DOWN:
                    current_block["position"][1] += 1
                elif event.key == pygame.K_SPACE:
                    current_block["rotation"] = (current_block["rotation"] + 1) % len(current_block["shape"])
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()