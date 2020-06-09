import keyboard
from threading import Thread
import pyfiglet
import time

#Config
last_key = ''
ping = 0.225
DirUp = 'Home'
DirDown = 'End'
DirLeft = 'Delete'
DirRight = 'Page Down'
WPkey = 'F1'
PScalpelkey = 'q'

#Welcome
fast_ascii = pyfiglet.figlet_format("Fast Macro Example")
print(fast_ascii)

def KeyCheck():
    print('[#] KeyCheck.Thread - Started! ')
    while True:
        global last_key
        if (keyboard.is_pressed('Left Arrow')):
            last_key = 'Left Arrow'
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('Right Arrow')):
            last_key = 'Right Arrow'
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('Up Arrow')):
            last_key = 'Up Arrow'
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('Down Arrow')):
            last_key = 'Down Arrow'
            print(last_key)
            time.sleep(0.15)

def ComboWP():
    print('[#] WP/Punish.Thread - Started! \n')
    while True:
        if (keyboard.is_pressed(WPkey) and last_key == 'Left Arrow'):
            time.sleep(1 + ping)
            keyboard.press_and_release(DirRight)
            time.sleep(0.1)
            keyboard.press_and_release(PScalpelkey)
        elif (keyboard.is_pressed(WPkey) and last_key == 'Right Arrow'):
            time.sleep(1 + ping)
            keyboard.press_and_release(DirLeft)
            time.sleep(0.1)
            keyboard.press_and_release(PScalpelkey)
        elif (keyboard.is_pressed(WPkey) and last_key == 'Up Arrow'):
            time.sleep(1 + ping)
            keyboard.press_and_release(DirDown)
            time.sleep(0.1)
            keyboard.press_and_release(PScalpelkey)
        elif (keyboard.is_pressed(WPkey) and last_key == 'Down Arrow'):
            time.sleep(1 + ping)
            keyboard.press_and_release(DirUp)
            time.sleep(0.1)
            keyboard.press_and_release(PScalpelkey)

if __name__ == '__main__':
    Thread(target = KeyCheck).start()
    Thread(target = ComboWP).start()


