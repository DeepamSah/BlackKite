import pygame
import cartesianPlane

x1 = int(input("Enter the x1 point "))
y1 = int(input("Enter the y1 point "))
x2 = int(input("Enter the x2 point "))
y2 = int(input("Enter the y2 point "))
x3 = int(input("Enter the x3 point "))
y3 = int(input("Enter the y3 point "))
pygame.init()
x1 *= 10
x2 *= 10
x3 *= 10
y1 *= 10
y2 *= 10
y3 *= 10
screen = pygame.display.set_mode((900, 500))
graph = cartesianPlane.CartesianPlane(screen)

graph.zooming(100)

#Initialize the loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        graph.event_handling(event)
    
    graph.update()
    cartesianPlane.draw.circle(graph, (100, 200, 255),(0, 0), 10 )
    cartesianPlane.draw.line(graph, (255, 255, 255), (0, -255555), (0, 255555), 4)
    cartesianPlane.draw.line(graph, (255, 255, 255), (-255555, 0), (255555, 0), 4)

    cartesianPlane.draw.line(graph, (0, 250, 150), (x1, y1), (x2, y2), 3 )
    cartesianPlane.draw.line(graph, (0, 250, 150), (x2, y2), (x3, y3), 3)
    cartesianPlane.draw.line(graph, (0, 250, 150), (x3, y3), (x1, y1), 3)

    pygame.display.update()