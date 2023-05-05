import pygame
import time
import random

# 初始化 Pygame 模块
pygame.init()

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义屏幕尺寸和速度
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# 定义显示分数的字体
font_style = pygame.font.SysFont(None, 30)

# 定义显示分数的函数
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# 定义绘制蛇的函数
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# 定义主游戏循环
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # 设置初始蛇长
    snake_List = []
    Length_of_snake = 1

    # 初始化食物位置
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 检查蛇是否越界
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # 更新蛇的位置并显示屏幕
        x1 += x1_change
        y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    our_snake(snake_block, snake_List)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(snake_speed)

# 游戏结束时退出 Pygame
pygame.quit()
quit()




"""
这是一个简单的贪吃蛇游戏实现。游戏中的蛇可以在屏幕上移动，当吃到食物时长度会增加。如果蛇碰到屏幕边缘或自己的身体，游戏将结束。玩家可以按下 Q 键退出游戏，或者按下 C 键重新开始游戏。

你可以将此代码复制到你的开发环境中，并尝试运行。如果你有其他问题或需要进一步的帮助，请随时告诉我。
"""


"""
import pygame
import time
import random

# Initialize Pygame modules
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define screen size and speed
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Define font for displaying score
font_style = pygame.font.SysFont(None, 30)

# Define function for displaying score
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Define function for drawing the snake
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Define main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # Set initial snake length
    snake_List = []
    Length_of_snake = 1

    # Initialize position of food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake is out of bounds
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 
# Check if snake is out of bounds
if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
    game_close = True

# Update snake position and display screen
x1 += x1_change
y1 += y1_change
dis.fill(black)
pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
snake_Head = []
snake_Head.append(x1)
snake_Head.append(y1)
snake_List.append(snake_Head)

if len(snake_List) > Length_of_snake:
    del snake_List[0]

for x in snake_List[:-1]:
    if x == snake_Head:
        game_close = True

our_snake(snake_block, snake_List)
pygame.display.update()

if x1 == foodx and y1 == foody:
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    Length_of_snake += 1

clock.tick(snake_speed)

# Exit Pygame when game is over
pygame.quit()
quit()
"""