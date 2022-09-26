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
# from webdriver_manager.microsoft import EdgeChromiumDriverManager https://www.duolingo.com/settings/account?isLoggingIn=true

class Session():
    number_links = []
    numbers = []
    limit = 0
    link = ""
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
    new_session.numbers, new_session.number_links = GetQuackrNumberLinks(new_session.link, new_session.limit, new_session.driver)

    return new_session

def SaveSession(session):
    pass

def LoadSession(session_path):
    pass

#Quackr
def GetAllQuackrMessages(session, phone_number_link, message_index):
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
        _message.recieved = msgs[0].text
        _message.sender = msgs[1].text
        _message.message = msgs[2].text

        messages.append(_message)

    return messages

def GetQuackrMessage(session, phone_number_link, message_index):
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
        _message.recieved = msgs[0].text
        _message.sender = msgs[1].text
        _message.message = msgs[2].text

        messages.append(_message)

    return messages[message_index]

def FindQuackrMessage(session, phone_number_link, substring):
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
        _message.recieved = msgs[0].text
        _message.sender = msgs[1].text
        _message.message = msgs[2].text
        
        if substring in _message.message:
            print(_message.message)
        else:
            continue

        messages.append(_message)

    return messages

def GetQuackrNumberLinks(_link, _limit, _driver):
    
    _number_links = []
    _numbers = []
    headers = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0")]

    driver = _driver
    driver.get(_link)
    sleep(5)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    s1 = soup.find("div", id="wrapper")

    i = 0
    for link in s1.find_all('a', attrs={'href': re.compile("^/temporary-numbers/sweden/")}):
        number_link = link.get('href')

        if link in _number_links:
            pass
        else:
            if i < _limit:
                __link = main_link + link.get('href')
                __number = link.get('href').split('/')[3]
                
                print(__link + " | " + __number)

                _number_links.append(__link)
                _numbers.append(__number)
                i += 1

    return _numbers, _number_links