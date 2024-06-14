import pygame
from pygame_widgets.button import Button
import pygame_widgets

pygame.init()

screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption("Click Counter")

running = True

screen.fill((0, 255, 255))

click = 0

def clicked():
    global click
    click += 1
    print(click)

button = Button(
    screen, 50,50, 300, 150, 
    text='Click Me',  
    fontSize=50, 
    margin=20,
    inactiveColour=(255, 0, 0),
    hoverColour=(220, 0, 0),
    pressedColour=(0, 200, 20), 
    radius=20,
    onClick=clicked
)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 255, 255))
    pygame_widgets.update(button) 

    font = pygame.font.SysFont("arial", 40, True)
    text = font.render("Click:"+str(click), True, (0,0,0))
    screen.blit(text, (150, 210))
    pygame.display.update()