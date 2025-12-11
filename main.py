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
