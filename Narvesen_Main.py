from email import message
from optparse import Option
from random import random, uniform
from socket import MSG_MCAST
from tracemalloc import start

from numpy import False_
import automation.bluestacks.system as bssystem
import automation.bluestacks.macro as bsmacro

import automation.sms.quackr_io as quackr 
from automation.sms.quackr_io import *

import automation.sms.temp_number_com as tnc
from automation.sms.temp_number_com import *

import pyautogui
import psutil
import win32gui

#Creates new autmation session
# quackr_session = quackr.NewSession("https://quackr.io/temporary-numbers/sweden", 39)

def Start():
    bssystem.LaunchApp('Narvesen', 'Narvesen App Player')

Start()

tnc_session_sweden = tnc.NewSession("Sweden", 9)
tnc_session_finland = tnc.NewSession("Finland", 10)
# quackr_session_sweden = quackr.NewSession("Sweden")
# quackr_session_finland = quackr.NewSession("Finland")

# print(str(len(tnc_session_sweden.numbers) + len(tnc_session_finland.numbers) + len(quackr_session_sweden.numbers) + len(quackr_session_finland.numbers)))

#Opens bluestacks/selects it
# bssystem.OpenBluestacks()

#Macro for registering
register_macro = bsmacro.Macro()
Register = bsmacro.CreateKey(bsmacro.Key(), 'r', 1)
Select_Country_Code = bsmacro.CreateKey(bsmacro.Key(), 'n', 0.75)
Select_Finland = bsmacro.CreateKey(bsmacro.Key(), 's', 0.75)
Over_13_Years_Of_Age = bsmacro.CreateKey(bsmacro.Key(), 'a', 0.5)
register_macro.keys = [Register, Select_Country_Code, Select_Finland, Over_13_Years_Of_Age]

#Get Pin
get_pin_macro = bsmacro.Macro()
Next_1 = bsmacro.CreateKey(bsmacro.Key(), 'i', 2)
Next_2 = bsmacro.CreateKey(bsmacro.Key(), 'i', 2)
get_pin_macro.keys = [Next_1, Next_2]

#Continue to settings
continue_macro = bsmacro.Macro()
Next_1 = bsmacro.CreateKey(bsmacro.Key(), 'i', 3)
Next_2 = bsmacro.CreateKey(bsmacro.Key(), 'i', 3)
Options = bsmacro.CreateKey(bsmacro.Key(), 'e', 2)
Settings = bsmacro.CreateKey(bsmacro.Key(), 'p', 2)
MoreDetails = bsmacro.CreateKey(bsmacro.Key(), 'm', 2)
ImNotARobot = bsmacro.CreateKey(bsmacro.Key(), 'h', 2)
LogIn = bsmacro.CreateKey(bsmacro.Key(), 'f', 2)
SelectPinbar = bsmacro.CreateKey(bsmacro.Key(), 'h',2)
continue_macro.keys = [Next_1, Next_2, Options, Settings, MoreDetails, ImNotARobot, LogIn, SelectPinbar]

#Delete account macro
finish_delete_macro = bsmacro.Macro()
DeleteProfile1 = bsmacro.CreateKey(bsmacro.Key(), 'enter', 2)
DeleteProfile2 = bsmacro.CreateKey(bsmacro.Key(), '9', 2)
Confirm1 = bsmacro.CreateKey(bsmacro.Key(), 'x', 2)
Confirm2 = bsmacro.CreateKey(bsmacro.Key(), 'x', 2)
ReturnToStart = bsmacro.CreateKey(bsmacro.Key(), 'e', 2)
finish_delete_macro.keys = [DeleteProfile1, DeleteProfile2, Confirm1, Confirm2, ReturnToStart]

def LogInFunc(i, _session):
    #Does all the necessary stuff before typing in the number
    bsmacro.RunMacro(register_macro)

    #Types in number
    current_number = _session.numbers[i]
    pyautogui.typewrite(str(current_number), uniform(0.1, 0.5))

    #Runs a macro after typing in the number
    bsmacro.RunMacro(get_pin_macro)

    #Waits a time  
    sleep(4)

    #Attempts to get the pin sent by Narvesen
    messages = tnc.FindTMCMessage(_session, _session.number_links[i], 'Velkommen til Narvesen-appen!')
    
    while len(messages) <= 0:
        sleep(0.3)
        messages = tnc.FindTMCMessage(_session, _session.number_links[i], 'Velkommen til Narvesen-appen!')
    
    newest_message = messages[0]
    newest_message_pin = newest_message.message.split(' ')[2]
    pyautogui.typewrite(newest_message_pin, uniform(0.1, 0.5))

def DeleteAccount(i, _session):
    #Continues to menu
        bsmacro.RunMacro(continue_macro)
        
        #Waits for deletion pin
        sleep(4)

        __messages = tnc.FindTMCMessage(_session, _session.number_links[i], 'PIN: ')
        
        subst = 'PIN: '
        has6PinCode = False
        while has6PinCode == False:
            sleep(1)
            print("Attempting...")
            messages = tnc.GetAllTMCMessages(_session, _session.number_links[i])
            for message in messages:
                if message.sender == "Narvesen":
                    if len(message.message.split(' ')) == 2:
                        has6PinCode = True
                        pyautogui.typewrite(message.message.split(' ')[1])
                        break


        bsmacro.RunMacro(finish_delete_macro)

for i in range(7, 10):
    LogInFunc(i, tnc_session_finland)
    DeleteAccount(i, tnc_session_finland)