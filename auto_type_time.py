from pynput.keyboard import Controller
import time

keyboard = Controller()
current_time = time.strftime("%H:%M")

for char in current_time:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
