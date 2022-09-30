from smtplib import OLDSTYLE_AUTH
from time import sleep

import win32gui

import PIL
import psutil
import pyautogui
from PIL import Image

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
    new_instance_position = pyautogui.locateOnScreen(r'E:\Projects\Automation\automation\bluestacks\images\new_instance.png', 0.9)
    pyautogui.click(new_instance_position)
    print(new_instance_position)

#Launching/Starting
def OpenBluestacks():
    pyautogui.press('win')
    sleep(0.1)
    pyautogui.typewrite("bluestacks 5")
    sleep(0.1)
    pyautogui.press('enter')

def LaunchApp(App_Name, Instance_Name):
    if "HD-Player.exe" in (p.name() for p in psutil.process_iter()):
        SetFocusToBluestacks(Instance_Name)
    else:
        pyautogui.press('win')
        sleep(0.1)
        pyautogui.typewrite(App_Name + " - " + Instance_Name, 0.1)
        sleep(0.1)
        pyautogui.press('enter')

#Handling
def SetFocusToBluestacks(Instance_Name):
    toplist = []
    winlist = []
    def enum_callback(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_callback, toplist)
    BlueStacks = [(hwnd, title) for hwnd, title in winlist if Instance_Name.lower() in title.lower()]
    # just grab the first window that matches
    BlueStacks = BlueStacks[0]
    # use the window handle to set focus
    win32gui.SetForegroundWindow(BlueStacks[0])