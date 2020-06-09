import keyboard
from threading import Thread
import pyfiglet
import time

#Config
last_key = '' #do not change
ping = 0.15 #your ping 100ping = 0.1 , 150ping = 0.15 etc.
DirUp = 'Home' #Direction Up Hotkey
DirDown = 'End' #Direction Down Hotkey
DirLeft = 'Delete' #Direction Left Hotkey
DirRight = 'Page Down' #Direction Right Hotkey
MoveUp = 'Up Arrow' #Move Up Hotkey
MoveDown = 'Down Arrow' #Move Down Hotkey
MoveLeft = 'Left Arrow' #Move Left Arrow
MoveRight = 'Right Arrow' #Move Right Arrow
WPkey = 'F1' #Water Prison Hotkey
PScalpelkey = 'q' #Poison Scalpel Hotkey

#Welcome
fast_ascii = pyfiglet.figlet_format("Fast Macro Example")
print(fast_ascii)

def KeyCheck():
    print('[#] KeyCheck.Thread - Started! ')
    while True:
        global last_key
        if (keyboard.is_pressed('MoveLeft')):
            last_key = 'Left Arrow' #do not change
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('MoveRight')):
            last_key = 'Right Arrow' #do not change
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('MoveUp')):
            last_key = 'Up Arrow' #do not change
            print(last_key)
            time.sleep(0.15)
        elif(keyboard.is_pressed('MoveDown')):
            last_key = 'Down Arrow' #do not change
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


