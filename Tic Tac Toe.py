import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (5, 255,255), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (5, 255,255), (400, 0), (400, 600), 5)

    pygame.draw.line(screen, (5, 255,255), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (5, 255,255), (0, 400), (600, 400), 5)
    
    key, key1 = pygame.mouse.get_pos()
    print(key, key1)

    if event.type == pygame.MOUSEBUTTONUP:
        (pow, pow1) = pygame.mouse.get_pos()
        s = (pow, pow1)

    font = pygame.font.SysFont("Arial", 50)
    text = font.render("he", True, (255,255, 0))
    text.blit(screen, (250, 250), 5)
    pygame.display.flip()

    pygame.display.update()
