from calendar import HTMLCalendar
from cgitb import text
from posixpath import split
from bs4 import BeautifulSoup
import re

from time import sleep as sleep

#Selenium
from selenium import webdriver

#Firefox Selenium
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

#Chrome Selenium
# from selenium.webdriver.chrome.options import Options as ChromiumOptions
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

#Egde Selenium
# from selenium.webdriver.edge.options import Options as ChromiumOptions
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager https://www.duolingo.com/settings/account?isLoggingIn=true

class Session():
    number_links = []
    numbers = []
    pages_amount = 0
    link = ""
    service = Service
    driver = webdriver.Firefox

class Message():
    recieved = ""
    sender = ""
    message = ""

global main_link
main_link = "https://www.temp-number.com/"

#Sessions
def NewSession(_link, _page_amount):
    new_session = Session()
    
    options = FirefoxOptions()
    options.add_argument("--headless")
    new_session.service = Service(GeckoDriverManager().install())
    new_session.driver = webdriver.Firefox(service=new_session.service, options=options)

    new_session.pages_amount = _page_amount
    new_session.link = _link
    new_session.numbers, new_session.number_links, *other = GetTMCInfo(new_session.pages_amount, new_session.link, new_session.driver)

    return new_session

def SaveSession(session):
    pass

def LoadSession(session_path):
    pass

#Temp Number Com - TMC
def GetAllTMCMessages(session, phone_number_link):
    #Sets what the message to a message class
    message = Message
    messages = []

    driver = session.driver
    driver.get(phone_number_link)

    msg_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/section/div/div/div/div/div')

    #Gets the text from the three elements in the msg element    
    for msg_element in msg_elements:
        sender_element = msg_element.find_element(By.XPATH, './i')
        recieved_element = msg_element.find_element(By.XPATH, './div[1]')
        message_element = msg_element.find_element(By.XPATH, './div[2]')

        _message = Message()
        _message.recieved = sender_element.text
        _message.sender = recieved_element.text
        _message.message = message_element.text

        messages.append(_message)

    return messages

def GetTMCMessage(session, phone_number_link, message_index):
    #Sets what the message to a message class
    message = Message
    messages = []

    driver = session.driver
    driver.get(phone_number_link)

    msg_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/section/div/div/div/div/div')

    #Gets the text from the three elements in the msg element    
    for msg_element in msg_elements:
        sender_element = msg_element.find_element(By.XPATH, './i')
        recieved_element = msg_element.find_element(By.XPATH, './div[1]')
        message_element = msg_element.find_element(By.XPATH, './div[2]')

        _message = Message()
        _message.recieved = sender_element.text
        _message.sender = recieved_element.text
        _message.message = message_element.text

        messages.append(_message)

    return messages[message_index]
    

def FindTMCMessage(session, phone_number_link, substring):
    #Sets what the message to a message class
    message = Message
    messages = []

    driver = session.driver
    driver.get(phone_number_link)

    msg_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/section/div/div/div/div/div')

    #Gets the text from the three elements in the msg element    
    for msg_element in msg_elements:
        sender_element = msg_element.find_element(By.XPATH, './i')
        recieved_element = msg_element.find_element(By.XPATH, './div[1]')
        message_element = msg_element.find_element(By.XPATH, './div[2]')

        _message = Message()
        _message.recieved = sender_element.text
        _message.sender = recieved_element.text
        _message.message = message_element.text
        
        if substring in _message.message:
            pass
        else:
            continue

        messages.append(_message)

    return messages

def GetTMCInfo(_page_amount, _link, _driver):
    _page_links = GetTMCPageLinks(_page_amount, _link)
    _number_links = GetTMCNumberLinks(_page_links, _driver)
    _numbers = GetTMCNumbers(_number_links)
    # headers = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0")]

    return _numbers, _number_links, _page_links

def GetTMCPageLinks(_page_amount, _link):
        _page_links = []
 
        #Generates a page url based off of how many pages are input
        for i in range(0, _page_amount):
            _page_link = _link[:(len(_link)-1)] + str(i + 1)
            _page_links.append(_page_link)

        return _page_links

def GetTMCNumberLinks(_page_links, _driver):
    _number_links = []

    for page in _page_links:
        _driver.get(page)
        number_container = _driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/section/div/div/a')
        i = 0
        for number_link_element in number_container:
            number_link = number_link_element.get_attribute('href')
            _number_links.append(number_link)
            i += 1
    
    return _number_links

def GetTMCNumbers(_number_links):
    _numbers = []
    i = 0
    for number in _number_links:
        # print(number.split('/')[3].split('=')[2][2:][:9] + " | " + str(i + 1))
        i += 1
        _numbers.append(number.split('/')[3].split('=')[2][2:][:9])

    return _numbers