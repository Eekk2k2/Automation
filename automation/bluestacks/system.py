from time import sleep
import pyautogui

def OpenBluestacks():
    pyautogui.press('win')
    sleep(0.1)
    pyautogui.typewrite("bluestacks 5")
    sleep(0.1)
    pyautogui.press('enter')

def Type(string):
    pyautogui.typewrite(string)

def LaunchApp(index):
    if (index <= 9):
        pyautogui.press(str(index))
    else:
        pyautogui.keyDown('shift')
        pyautogui.press(str(index))
        pyautogui.keyUp('shift')

def Fullscreen(sleep_time):
    sleep(sleep_time)
    pyautogui.press('f11')