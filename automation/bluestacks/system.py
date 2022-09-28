from smtplib import OLDSTYLE_AUTH
from time import sleep
import pyautogui

global main_path
main_path = r"C:\Users\Eskil\Downloads\Narvesen_v6.0.1_apkpure.com"

#Installing and Instance handler
def InstallFirstApkInPath(_path):
    pyautogui.hotkey('ctrlleft', 'shiftleft', 'b')
    sleep(0.2)
    pyautogui.hotkey('alt', 'd')
    sleep(0.2)
    pyautogui.typewrite(_path)
    sleep(0.2)
    pyautogui.press('enter')
    sleep(0.2)
    pyautogui.press('tab')
    sleep(0.2)
    pyautogui.press('tab')
    sleep(0.2)
    pyautogui.press('tab')
    sleep(0.2)
    pyautogui.press('tab')
    sleep(0.2)
    pyautogui.press('space')
    sleep(0.2)
    pyautogui.press('enter')

def CreateNewInstance(name):
    sleep(5)
    pyautogui.hotkey('ctrlleft', 'shiftleft', '8')
    sleep(5)
    new_instance_position = pyautogui.locateCenterOnScreen(r'..\images\new_instance.png')
    print(new_instance_position)

#Launching/Starting
def OpenBluestacks():
    pyautogui.press('win')
    sleep(0.1)
    pyautogui.typewrite("bluestacks 5")
    sleep(0.1)
    pyautogui.press('enter')

def LaunchApp(index):
    if (index <= 9):
        pyautogui.press(str(index))
    else:
        pyautogui.keyDown('shift')
        pyautogui.press(str(index))
        pyautogui.keyUp('shift')

# InstallFirstApkInPath(main_path)
CreateNewInstance("deez")