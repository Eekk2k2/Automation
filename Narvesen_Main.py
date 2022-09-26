from optparse import Option
from random import random, uniform
from socket import MSG_MCAST
import automation.bluestacks.system as bssystem
import automation.bluestacks.macro as bsmacro

import automation.sms.quackr_io as quackr 
from automation.sms.quackr_io import *

import automation.sms.temp_number_com as tmc
from automation.sms.temp_number_com import *

import pyautogui

#Creates new autmation session
# quackr_session = quackr.NewSession("https://quackr.io/temporary-numbers/sweden", 39)

tmc_session_sweden = tmc.NewSession("Sweden", 9)
tmc_session_finland = tmc.NewSession("Finland", 10)
quackr_session_sweden = quackr.NewSession("Sweden")
quackr_session_finland = quackr.NewSession("Finland")

# print(len(quackr_session_finland.numbers))
# print(str(len(tmc_session_sweden.numbers) + len(tmc_session_finland.numbers) + len(quackr_session_sweden.numbers) + len(quackr_session_finland.numbers)))


# quackr_session_finland = quackr.NewSession("https://quackr.io/temporary-numbers/finland", 5)

# print(len(tmc_session_sweden.numbers))
# print(len(tmc_session_sweden.numbers))
# print(len(quackr_session_sweden))
#Opens bluestacks/selects it
# bssystem.OpenBluestacks()

# def LogInLogOut(i):
#     #Selects link nr 1
#     link = quackr_session.number_links[i]

    # #Macro for registering
    # register_macro = bsmacro.Macro()
    # Register = bsmacro.CreateKey(bsmacro.Key(), 'r', 0.5)
    # Select_Country_Code = bsmacro.CreateKey(bsmacro.Key(), 'n', 0.75)
    # Select_Sweden = bsmacro.CreateKey(bsmacro.Key(), 's', 0.75)
    # Over_13_Years_Of_Age = bsmacro.CreateKey(bsmacro.Key(), 'a', 0.5)
    # register_macro.keys = [Register, Select_Country_Code, Select_Sweden, Over_13_Years_Of_Age]
    # bsmacro.RunMacro(register_macro)

    # number_string = ""
    # number_string = session.numbers[i]

    # #Types in number
    # pyautogui.typewrite(str(number_string)[2:], uniform(0.1, 0.5))

    # get_pin_macro = bsmacro.Macro()
    # Next_1 = bsmacro.CreateKey(bsmacro.Key(), 'i', 1)
    # Next_2 = bsmacro.CreateKey(bsmacro.Key(), 'i', 0.5)
    # get_pin_macro.keys = [Next_1, Next_2]
    # bsmacro.RunMacro(get_pin_macro)

    # sleep(10)

    # messages = quackr.FindQuackrMessage(session, session.number_links[i], 'Velkommen til Narvesen-appen!')
    # newest_message = messages[0]
    # newest_message_pin = newest_message.message.split(' ')[2]
    # pyautogui.typewrite(newest_message_pin, uniform(0.1, 0.5))

    # continue_macro = bsmacro.Macro()
    # Next_1 = bsmacro.CreateKey(bsmacro.Key(), 'i', 1)
    # Next_2 = bsmacro.CreateKey(bsmacro.Key(), 'i', 0.5)
    # Options = bsmacro.CreateKey(bsmacro.Key(), 'e', 1)
    # Settings = bsmacro.CreateKey(bsmacro.Key(), 'p', 1)
    # MoreDetails = bsmacro.CreateKey(bsmacro.Key(), 'm', 1)
    # ImNotARobot = bsmacro.CreateKey(bsmacro.Key(), 'h', 2)
    # LogIn = bsmacro.CreateKey(bsmacro.Key(), 'f', 1)
    # SelectPinbar = bsmacro.CreateKey(bsmacro.Key(), 'h',1)
    # continue_macro.keys = [Options, Settings, MoreDetails, ImNotARobot, LogIn, SelectPinbar]
    # bsmacro.RunMacro(continue_macro)

    # sleep(10)

    # messages = quackr.FindQuackrMessage(session, session.number_links[i], 'PIN: ')
    # newest_message = messages[0]
    # if newest_message.sender == "Narvesen":
    #     newest_message_pin = newest_message.message.split(' ')[1]
    #     pyautogui.typewrite(newest_message_pin, uniform(0.1, 0.5))
    # else:
    #     print("No message")

    # finish_delete_macro = bsmacro.Macro()
    # DeleteProfile = bsmacro.CreateKey(bsmacro.Key(), 'enter', 0.5)
    # DeleteProfile = bsmacro.CreateKey(bsmacro.Key(), '9', 0.5)
    # Confirm = bsmacro.CreateKey(bsmacro.Key(), 'x', 0.5)
    # Confirm = bsmacro.CreateKey(bsmacro.Key(), 'x', 0.5)
    # finish_delete_macro.keys = [DeleteProfile, Confirm]
    # bsmacro.RunMacro(finish_delete_macro)

# LogInLogOut(5)