import pygame
import random

pygame.init()

# Constants
SPRITE_RADIUS = 15
PIPE_WIDTH = 50
GAP_HEIGHT = 200
GRAVITY = 10
JUMP_SPEED = -60
PIPE_SPEED = 5
PIPE_ADD_INTERVAL = 1500  # milliseconds
SCORE_FONT_SIZE = 36

# Colors
BACKGROUND_COLOR = (135, 206, 250)  # Light blue
PIPE_COLOR = (0, 128, 0)  # Dark green
SPRITE_COLOR = (0, 0, 0)  # Black
SCORE_COLOR = (255, 255, 255)  # White

# Initialize the screen
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, SCORE_FONT_SIZE)

# Function to draw the sprite
def draw_sprite(y):
    sprite_pos = (sprite_x, y)
    pygame.draw.circle(screen, SPRITE_COLOR, sprite_pos, SPRITE_RADIUS)

# Function to draw a pipe
def draw_pipe(x, height):
    top_pipe_rect = pygame.Rect(x, 0, PIPE_WIDTH, height)
    bottom_pipe_rect = pygame.Rect(x, height + GAP_HEIGHT, PIPE_WIDTH, 500 - height - GAP_HEIGHT)
    pygame.draw.rect(screen, PIPE_COLOR, top_pipe_rect)
    pygame.draw.rect(screen, PIPE_COLOR, bottom_pipe_rect)

# Function to detect collision between sprite and pipes
def check_collision():
    sprite_rect = pygame.Rect(sprite_x - SPRITE_RADIUS, sprite_y - SPRITE_RADIUS, SPRITE_RADIUS * 2, SPRITE_RADIUS * 2)
    for pipe in pipes:
        top_pipe_rect = pygame.Rect(pipe['x'], 0, PIPE_WIDTH, pipe['height'])
        bottom_pipe_rect = pygame.Rect(pipe['x'], pipe['height'] + GAP_HEIGHT, PIPE_WIDTH, 500 - pipe['height'] - GAP_HEIGHT)
        if sprite_rect.colliderect(top_pipe_rect) or sprite_rect.colliderect(bottom_pipe_rect):
            return True
    return False

# Initialize game variables
sprite_x = 100
sprite_y = 500 // 2
pipes = []
last_pipe_added_time = 0
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sprite_y += JUMP_SPEED  # Move the sprite upwards when spacebar is pressed

    screen.fill(BACKGROUND_COLOR)  # Fill the screen with background color

    # Draw the sprite
    draw_sprite(sprite_y)

    # Add pipes at regular intervals
    if pygame.time.get_ticks() - last_pipe_added_time > PIPE_ADD_INTERVAL:
        pipe_height = random.randint(50, 500 - GAP_HEIGHT - 50)
        pipes.append({'x': 800, 'height': pipe_height})
        last_pipe_added_time = pygame.time.get_ticks()

    # Move pipes and draw them
    for pipe in pipes[:]:
        pipe['x'] -= PIPE_SPEED
        draw_pipe(pipe['x'], pipe['height'])
        if pipe['x'] + PIPE_WIDTH < 0:
            pipes.remove(pipe)
            score += 1

    # Apply gravity to the sprite
    sprite_y += GRAVITY

    # Check for collision with pipes or going out of bounds
    if sprite_y - SPRITE_RADIUS < 0 or sprite_y + SPRITE_RADIUS > 500 or check_collision():
        running = False

    # Display the score
    score_text = font.render(f'Score: {score}', True, SCORE_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

# Game over
game_over_text = font.render('Game Over', True, SCORE_COLOR)
screen.blit(game_over_text, (800 // 2 - 100, 500 // 2 - 50))
score_text = font.render(f'Final Score: {score}', True, SCORE_COLOR)
screen.blit(score_text, (800 // 2 - 100, 500 // 2))
pygame.display.update()

# Wait for a moment before exiting
pygame.time.wait(2000)

pygame.quit()
