import keyboard # pip install keyboard
import mouse # pip install mouse
import time

def change():
    global work
    work = not work

work = False
hotkey = 'alt'
keyboard.add_hotkey(hotkey, change)

while True:
    if work:
        mouse.click(button="left")
        time.sleep(0.1)