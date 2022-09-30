import win32com.client as win32

from posixpath import split
from bs4 import BeautifulSoup
import re

from time import sleep as sleep

#Selenium
from selenium import webdriver

#Chrome Selenium
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'eekk2k2@gmail.com'
mail.Subject = 'Subjectify women'
mail.Body = 'Body body body body'

mail.Send()

# class Session():
#     emails = []
#     email_links = []
#     service = Service
#     driver = webdriver.Chrome

# class Email():
#     recieved = ""
#     sender = ""
#     message = ""

# global main_link
# main_link = "https://www.outlook.com"

# #Sessions
# def NewSession():
#     new_session = Session()
    
#     options = ChromeOptions()
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-web-security")
#     options.add_argument("--allow-running-insecure-content")
#     # options.add_argument("--headless")
#     new_session.service = Service(ChromeDriverManager().install())
#     new_session.driver = webdriver.Chrome(service=new_session.service, options=options)

#     # new_session.emails, new_session.email_links = GetGmailMails(new_session.driver)

#     return new_session

# def SaveSession(session):
#     pass

# def LoadSession(session_path):
#     pass

# def GmailLogIn(email, password, driver):
#     driver = driver
#     driver.get(main_link)
#     sleep(5)
    
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'lxml')

#     s1 = soup.find("body")
#     s2 = s1.find("div", id="initialView")

#     print(s1)

# #Gmail
# def FindGmailMail(session, phone_number_link, substring):
#     #Sets what the message to a message class
#     email = Email
#     emails = []

#     driver = session.driver
#     driver.get(phone_number_link)
#     sleep(5)

# def GetGmailMails(_driver):
    
#     _email_links = []
#     _emails = []
#     headers = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0")]

#     driver = _driver
#     driver.get(main_link)
#     sleep(5)
    
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'lxml')

#     s1 = soup.find("div", {"class":"ae4 aDM nH oy8Mbf"}, id=":10")

#     print(s1.prettify())

#     # i = 0
#     # for link in s1.find_all('a', attrs={'href': re.compile("^/temporary-numbers/sweden/")}):
#     #     number_link = link.get('href')

#     #     if link in _number_links:
#     #         pass
#     #     else:
#     #         if i < _limit:
#     #             __link = main_link + link.get('href')
#     #             __number = link.get('href').split('/')[3]
                
#     #             print(__link + " | " + __number)

#     #             _number_links.append(__link)
#     #             _numbers.append(__number)
#     #             i += 1

#     return _emails, _email_links

# session = NewSession()
# GmailLogIn("", "", session.driver)