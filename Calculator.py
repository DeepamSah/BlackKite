# this is a calculator /\
import pygame 
import pygame_widgets 
from pygame_widgets.button import Button

pygame.init()

screen = pygame.display.set_mode((450, 640))

value = 0  # Initial value for the calculator
current_operator = None
operator_functions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '×': lambda x, y: x * y,
    '÷': lambda x, y: x / y if y != 0 else "Error"  # Avoid division by zero
}

def key_pressed(value_on_click):
    global value, current_operator, first_value
    if isinstance(value_on_click, int):
        # Handle digits
        if current_operator is None:
            value = value * 10 + value_on_click
        else:
            first_value = value  # Store the first value
            value = value_on_click  # Start a new value for the second operand
    elif value_on_click == "=":
        if current_operator is not None:
            value = operator_functions[current_operator](first_value, int(value))  # Use stored first value
            current_operator = None
            first_value = None  # Reset for the next calculation
    elif value_on_click in ["+", "-", "×", "÷"]:
        current_operator = value_on_click
    elif value_on_click == "C":
        value = 0
        current_operator = None
        first_value = None  # Reset for the next calculation
    print("Value:", value)

           
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((32,32,32))

    display_rect = pygame.draw.rect(screen, (225,225,225), (20, 60, 415, 130), 5, 5 )

    # Buttons 
    button7 = Button(
        screen, 20, 200, 100, 80, text = "7",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(7)
    )

    button8 = Button(
        screen, 125, 200, 100, 80, text = "8",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(8)
    )

    button9 = Button(
        screen, 230, 200, 100, 80, text = "9",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(9)
    )

    button4 = Button(
        screen, 20, 285, 100, 80, text = "4",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(4)
    )

    button5 = Button(
        screen, 125, 285, 100, 80, text = "5",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(5)
    )

    button6 = Button(
        screen, 230, 285, 100, 80, text = "6",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(6)
    )

    button1 = Button(
        screen, 20, 370, 100, 80, text = "1",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(1)
    )

    button2 = Button(
        screen, 125, 370, 100, 80, text = "2",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(2)
    )

    button3 = Button(
        screen, 230, 370, 100, 80, text = "3",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(3)
    )

    button0 = Button(
        screen, 20, 455, 205, 80, text = "0",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(0)
    )

    buttonDot = Button(
        screen, 230, 455, 100, 80, text = ".",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed(".")
    )

    buttonPlus = Button(
        screen, 335, 200, 100, 80, text = "+",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed("+")
    )

    buttonMinus = Button(
        screen, 335, 285, 100, 80, text = "-",
        fontSize=60, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed("-")
    )

    buttonMultiply = Button(
        screen, 335, 370, 100, 80, text = "×",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed("×")
    )

    buttonDivide = Button(
        screen, 335, 455, 100, 80, text = "÷",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed("÷")
    ) 

    buttonEqual = Button(
        screen, 230, 540, 205, 80,  text = "=",
        fontSize=50, 
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius = 10,
        onClick = lambda:  key_pressed("=")
    )

    buttonClear = Button(
        screen, 20, 540, 205, 80, text="C",
        fontSize=50,
        inactiveColour=(125, 125, 125),
        pressedColour=(110, 110, 110),
        radius=10,
        onClick=lambda: key_pressed("C")
    )
    

    # Display text
    display_rect_font = pygame.font.SysFont("arial", 100,True )
    display_rect_text = display_rect_font.render(str(value), True, (255, 255, 255))
    screen.blit(display_rect_text, (35, 75))
    
    # mouse pos
    mouse_pos = pygame.mouse.get_pos()
    mouse_font = pygame.font.SysFont("arial", 20,True)
    mouse_text = mouse_font.render(str(mouse_pos), True, (255, 255,255))
    mouse = mouse_text.get_rect()
    screen.blit(mouse_text, (0,0))

    pygame_widgets.update(Button)
    pygame.display.update()