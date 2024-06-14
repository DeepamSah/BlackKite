import pygame, random

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Ping Pong")

def quit_screen(score):
    import pygame

    pygame.init()

    screen = pygame.display.set_mode((900, 600))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Ping Pong")
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("calibri", 50, True)
    text = font.render("Your Score: " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (450, 300)
    screen.blit(text, text_rect)

    d_font = pygame.font.SysFont("calibri", 70, True)
    d_text = d_font.render("You Died!!", True, (255, 0, 0))
    screen.blit(d_text, (300, 40)) 
    
    clock.tick(100)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

score = 0

mover = pygame.rect.Rect(420, 500, 100, 10)

up_slab = pygame.rect.Rect(0, 70, 900, 10)

clock = pygame.time.Clock()

player_speed = 10

# Ball
ball_x = 468
ball_y = 100
ball_speed_x = 0  
ball_speed_y = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            
    screen.fill((0, 0, 0))

    # blit up_slab
    pygame.draw.rect(screen, (225, 225, 00), up_slab)

    # Score
    score_font = pygame.font.SysFont("times new roman", 30)
    score_text = score_font.render('Score : '+str(score), True, (225, 225, 225))
    score_rect = score_text.get_rect()
    screen.blit(score_text, score_rect)

    # Heading 
    heading_font = pygame.font.SysFont("calibri", 50, True)
    heading_text = heading_font.render("Ping Pong", True, (255, 255, 255))
    screen.blit(heading_text, (360, 10))

    # Mover 
    pygame.draw.rect(screen, (245, 255, 0), mover, 0, 4)

    # Mover move
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        mover.x -= player_speed
    if key[pygame.K_RIGHT]:
        mover.x += player_speed

    if mover.right > 900:
        mover.right = 900
    if mover.left < 0:
        mover.left = 0

    # Ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 8)

    if mover.colliderect(ball):
        ball_speed_y = -ball_speed_y  # Reverse the vertical direction
        score += 1
        ball_speed_x = random.randrange(-7, 7)

    # Ball move
    if ball.top <= up_slab.bottom:
        ball_speed_y = -ball_speed_y  

    if ball.right > 900:
        ball_speed_x = -ball_speed_x
    if ball.left < 0:
        ball_speed_x = -ball_speed_x

    if ball.bottom > 600:
        quit_screen(score)

    clock.tick(60)
    pygame.display.update()