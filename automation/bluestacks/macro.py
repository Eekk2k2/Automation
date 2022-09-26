from time import sleep
import pyautogui

class Macro:
    keys = []
    
class Key:
    key = ''
    wait_time = 0.5

def CreateKey(key_class, _key, _wait_time):
    key_class.key = _key
    key_class.wait_time = _wait_time
    return key_class

def RunBluestacksMacro(key1, key2):
    pyautogui.hotkey(key1, key2)

def RunMacro(Macro):
    for Key_Item in Macro.keys:
        pyautogui.press(Key_Item.key)
        sleep(Key_Item.wait_time)