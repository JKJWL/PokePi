from gpiozero import Button
import random
import Controller
from Game_Display import start_game_window
def main():
    start_game_window()
    button1 = Button(1)
    button2 = Button(2)
    button3 = Button(3)
    button4 = Button(4)
    print("Press Button to move ><^v")
    if Button.is_pressed:
        Controller.controls(Button.value)

if __name__ == "__main__":
    main()

#this is what I have so far will be 
#further updating as this concept is
#really fun never worked with a visual program in python so I am going to do it.