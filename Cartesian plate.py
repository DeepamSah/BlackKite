import pygame 

# Inputs
x1 = int(input("Enter the corrdinate of x1 "))
y1 = int(input("Enter the corrdinate of y1 "))
x2 = int(input("Enter the corrdinate of x2 "))
y2 = int(input("Enter the corrdinate of y2 "))
x3 = int(input("Enter the corrdinate of x3 "))
y3 = int(input("Enter the corrdinate of y3 "))
x4 = int(input("Enter the corrdinate of x4 "))
y4 = int(input("Enter the corrdinate of y4 "))

pygame.init()

screen= pygame.display.set_mode((900, 600))
pygame.display.set_caption("Cartesian Plane")

x= 5
y = 302
xx = 455
yy = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    # _____________________________________________________________________________ # 
    # y axis line 
    y_axis_start_x = 0
    y_axis_start_y = 300
    y_axis_start = (y_axis_start_x, y_axis_start_y)
    y_axis_end_x = 900
    y_axis_end_y = 300
    y_axis_end = (y_axis_end_x, y_axis_end_y)
    pygame.draw.line(screen, (255, 255, 255), y_axis_start, y_axis_end, 3)

    # x axis line 
    x_axis_start_x =450
    x_axis_start_y = 0
    x_axis_start = (x_axis_start_x, x_axis_start_y)
    x_axis_end_x = 450
    x_axis_end_y = 600
    x_axis_end = (x_axis_end_x, x_axis_end_y)
    pygame.draw.line(screen, (255, 255, 255),x_axis_start , x_axis_end , 3)

    # other lines loop
    startx = 0
    starty = 30
    endx =900
    endy = 30
    inx = 30
    iny = 0
    outx = 30
    outy = 600

    for _ in range(100):
        start = (startx, starty)
        end = (endx, endy)
        inz = (inx, iny)
        outz = (outx, outy)
        pygame.draw.line(screen, (250, 250, 250), start, end, 1)
        pygame.draw.line(screen, (250, 250, 250), inz, outz, 1)
        starty += 30
        endy += 30
        inx += 30
        outx += 30

    for i in range(-15, 15):
        font_x = pygame.font.SysFont("arial", 15, True)
        text_x = font_x.render(str(i), True, (200, 200, 0))
        screen.blit(text_x, (x, y))
        x+=30
    for j in range(10, -15, -1):
        font_x = pygame.font.SysFont("arial", 15, True)
        text_x = font_x.render(str(j), True, (200, 200, 0))
        screen.blit(text_x, (xx, yy))
        yy+=30
    pygame.draw.circle(screen, (200, 0, 0), (450, 300), 6)
    # _____________________________________________________________________________ #
    
    pygame.draw.line(screen, (0, 0, 255), (x1*30+450, 300 - y1*30), (x2*30+450, 300 - y2*30), 5)
    pygame.draw.line(screen, (0, 0, 255), (x2*30+450, 300 - y2*30), (x3*30+450, 300 - y3*30), 5)
    pygame.draw.line(screen, (0, 0, 255), (x4*30+450, 300 - y4*30), (x3*30+450, 300 - y3*30), 5)
    pygame.draw.line(screen, (0, 0, 255), (x1*30+450, 300 - y1*30), (x4*30+450, 300 - y4*30), 5)

    pygame.display.update()