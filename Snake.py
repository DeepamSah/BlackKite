import pygame
import random

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
running = True

snake = [pygame.Rect(450, 300, 30, 30)]
direction = "up"
score = 0

def spawn_fruit():
    while True:
        fruit_x, fruit_y = random.randrange(0, 870, BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT-BLOCK_SIZE, BLOCK_SIZE)
        fruit_rect = pygame.Rect(fruit_x, fruit_y, BLOCK_SIZE, BLOCK_SIZE)
        if not any(fruit_rect.colliderect(block) for block in snake):
            return fruit_rect

fruit = spawn_fruit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "down":
        direction = "up"
    elif keys[pygame.K_DOWN] and direction != "up":
        direction = "down"
    elif keys[pygame.K_LEFT] and direction != "right":
        direction = "left"
    elif keys[pygame.K_RIGHT] and direction != "left":
        direction = "right"

    if direction == "up":
        new_head = snake[0].move(0, -BLOCK_SIZE)
    elif direction == "down":
        new_head = snake[0].move(0, BLOCK_SIZE)
    elif direction == "left":
        new_head = snake[0].move(-BLOCK_SIZE, 0)
    elif direction == "right":
        new_head = snake[0].move(BLOCK_SIZE, 0)

    if new_head.colliderect(fruit):
        fruit = spawn_fruit()
        score += 1
    else:
        snake.pop()

    if any(new_head.colliderect(block) for block in snake) or not (0 <= new_head.x < SCREEN_WIDTH and 0 <= new_head.y < SCREEN_HEIGHT):
        running = False

    snake.insert(0, new_head)

    screen.fill((155, 255, 0))

    for block in snake:
        pygame.draw.rect(screen, (255, 0, 0), block)

    pygame.draw.circle(screen, (0, 0, 0), fruit.center, BLOCK_SIZE // 2)

    score_font = pygame.font.SysFont("arial", 30, True)
    score_text = score_font.render('Score: ' + str(score), True, (0, 100, 225))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(12)

pygame.quit()
