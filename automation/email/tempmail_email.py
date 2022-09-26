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

#Chrome Selenium
# from selenium.webdriver.chrome.options import Options as ChromiumOptions
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

#Egde Selenium
# from selenium.webdriver.edge.options import Options as ChromiumOptions
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Session():
    email = ""
    service = Service
    driver = webdriver.Firefox

class Message():
    recieved = ""
    sender = ""
    message = ""

global main_link
main_link = "https://quackr.io"

#Sessions
def NewSession(_link, _limit):
    new_session = Session()
    
    options = FirefoxOptions()
    options.add_argument("--headless")
    new_session.service = Service(GeckoDriverManager().install())
    new_session.driver = webdriver.Firefox(service=new_session.service, options=options)

    new_session.limit = _limit
    new_session.link = _link

    return new_session

def SaveSession(session):
    pass

def LoadSession(session_path):
    pass

#Temp-Mail
def GetAllTMMessages(session, phone_number_link, message_index):
    #Sets what the message to a message class
    message = Message
    messages = []

    driver = session.driver
    driver.get(phone_number_link)
    sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    #Walks through html code
    s1 = soup.find("div", id="wrapper")
    s2 = s1.find("messages", {"_nghost-serverapp-c20":""})
    s3 = s2.find("div", {"class":"column"}, {"_nghost-serverapp-c20":""})
    s4 = s3.find("table")
    s5 = s4.find("tbody")
    msg_elements = s5.find_all("tr")

    #Gets the text from the three elements in the msg element    
    for msg_element in msg_elements:
        msgs = msg_element.find_all("td")
        
        _message = Message()
        _message.time_ago = msgs[0].text
        _message.sender = msgs[1].text
        _message.message = msgs[2].text

        messages.append(_message)

    return messages