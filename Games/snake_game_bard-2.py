import python3-tk as tk

# Define the window size
WIDTH = 400
HEIGHT = 400

# Create the window
window = tk.Tk()
window.title("Snake Game")
window.geometry("%dx%d" % (WIDTH, HEIGHT))

# Create the canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create the snake
snake = []
snake.append((0, 0))
snake.append((0, 1))
snake.append((0, 2))

# Create the food
food = (100, 100)

# Draw the snake and the food
canvas.create_rectangle(snake[0][0], snake[0][1], snake[1][0], snake[1][1], fill="black")
canvas.create_rectangle(food[0], food[1], food[0] + 10, food[1] + 10, fill="red")

# Define the key bindings
UP = tk.W
DOWN = tk.S
LEFT = tk.A
RIGHT = tk.D

# Create a function to move the snake
def move_snake():
    global snake

    # Get the current direction of the snake
    direction = snake[-1] - snake[-2]

    # Move the snake in the specified direction
    if direction == (0, 1):
        snake.append((snake[-1][0], snake[-1][1] + 1))
    elif direction == (0, -1):
        snake.append((snake[-1][0], snake[-1][1] - 1))
    elif direction == (1, 0):
        snake.append((snake[-1][0] + 1, snake[-1][1]))
    elif direction == (-1, 0):
        snake.append((snake[-1][0] - 1, snake[-1][1]))

    # Remove the first part of the snake
    snake.pop(0)

    # Check if the snake has eaten the food
    if snake[-1] == food:
        # Grow the snake
        snake.append((snake[-1][0], snake[-1][1]))

        # Create a new food
        food = (
            int(random.randrange(0, WIDTH - 10)),
            int(random.randrange(0, HEIGHT - 10)),
        )

    # Check if the snake has hit itself or the edge of the window
    if snake[-1] in snake[:-1] or snake[-1][0] < 0 or snake[-1][0] >= WIDTH or snake[-1][1] < 0 or snake[-1][1] >= HEIGHT:
        # Game over
        window.destroy()

# Create a timer to move the snake every 100 milliseconds
timer = tk.Timer(100, move_snake)
timer.start()

# Start the main loop
window.mainloop()

