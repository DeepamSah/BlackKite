import time
import pygame
from plyer import notification

iterations = int(input("Enter the number of iterations "))

pygame.init()

def window():
    notification.notify(
        title= "Timer",
        message= "Its been 15 Mins",
        app_name= "Weather",
        app_icon= r"C:\Users\Deepam Sah\Desktop\Python Files\alarm.ico"
    )
    

def play_sound():
    pygame.mixer.music.load("C:\\Users\\Deepam Sah\\Desktop\\Python Files\\sound_file.wav")
    pygame.mixer.music.play()

def timer(interval, iterations):
    for _ in range(iterations):
        print("Timer Started:", time.strftime("%H:%M:%S", time.localtime()))
        play_sound()
        window()
        time.sleep(interval)

if __name__ == "__main__":
    interval = 10
    window()
    timer(interval, iterations)
