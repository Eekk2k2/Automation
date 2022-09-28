from posixpath import split
from bs4 import BeautifulSoup
import re

from time import sleep as sleep
from automation.sms.countrydata import Country
from automation.sms.countrydata import GetCountryDataByIndex
from automation.sms.countrydata import GetCountryDataByName

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
    limit = 0
    country = ""
    link = ""
    service = Service
    driver = webdriver.Firefox

class Message():
    recieved = ""
    sender = ""
    message = ""

global main_link
main_link = "https://quackr.io"

global page_link_start
page_link_start = "https://quackr.io/temporary-numbers/"

global page_link_end
page_link_end = ""

#Sessions
def NewSession(_country):
    new_session = Session()
    
    options = FirefoxOptions()
    options.add_argument("--headless")
    new_session.service = Service(GeckoDriverManager().install())
    new_session.driver = webdriver.Firefox(service=new_session.service, options=options)

    new_session.limit = 0
    new_session.country = _country
    new_session.link = page_link_start + _country + page_link_end
    new_session.numbers, new_session.number_links = GetQuackrInfo(new_session, new_session.limit, new_session.link, new_session.driver)

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
    print(phone_number_link)
    
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

def GetQuackrInfo(session, _limit, _link, _driver):
    _number_links = GetQuackrNumberLinks(session, _limit, _link, _driver)
    _numbers = GetQuackrNumbers(session, _number_links)

    return _numbers, _number_links

def GetQuackrNumberLinks(_session,_limit, _link, _driver):
    _number_links = []
    # headers = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0")]

    _driver.get(_link)
    number_container = _driver.find_elements(By.XPATH, '/html/body/app-root/div/div/main/country-page/section/div/div[2]/div')

    while len(number_container) <= 0:
        sleep(0.1)
        number_container = _driver.find_elements(By.XPATH, '/html/body/app-root/div/div/main/country-page/section/div/div[2]/div')

    for number_element in number_container:
        number_link = number_element.find_element(By.XPATH, './number-card/div/p[2]/a').get_attribute('href')
        _number_links.append(number_link)

    return _number_links

def GetQuackrNumbers(_session, _number_links):
    country = Country()
    country = GetCountryDataByName(_session)

    _numbers = []
    for _link in _number_links:
        number = _link.split('/')[5][len(country.CC):]
        # print(number)
        _numbers.append(number)
    return _numbers