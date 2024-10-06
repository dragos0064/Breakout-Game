import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_SIZE = 16
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)  # Added black for background

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Breakout Game')

# Paddle settings
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 10

# Ball settings
ball = pygame.Rect(paddle.x + paddle.width // 2, paddle.y - BALL_SIZE, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = 5 * random.choice((-1, 1)), -5

# Bricks setup with color layers
brick_colors = [RED, RED, ORANGE, ORANGE, GREEN, GREEN, YELLOW, YELLOW]
bricks = []
for y in range(8):  # 8 rows
    for x in range(10):  # 10 columns
        brick = pygame.Rect(x * (BRICK_WIDTH + 5) + 35, y * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append((brick, brick_colors[y % len(brick_colors)]))

# Game loop
clock = pygame.time.Clock()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= SCREEN_HEIGHT:
        print("Game Over")
        run = False

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick, color in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove((brick, color))
            ball_speed_y *= -1
            break

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
