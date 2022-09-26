from math import floor
from os import system
import os
from posixpath import split
from random import random, uniform, choice
import string
from bs4 import BeautifulSoup
import re
import numpy

from time import sleep as sleep

#Selenium
from selenium import webdriver

#Firefox Selenium
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 


#Chrome Selenium
# from selenium.webdriver.chrome.options import Options as ChromiumOptions
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

#Egde Selenium
# from selenium.webdriver.edge.options import Options as ChromiumOptions
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager https://www.duolingo.com/settings/account?isLoggingIn=true

class Session():
    email_name = "sverresteels"
    email_service = "@gmail.com"
    runs = 0
    service = Service
    driver = webdriver.Firefox

global main_link
main_link = "https://quackr.io"

#Sessions
def NewSession(email):
    new_session = Session()
    
    options = FirefoxOptions()
    # options.add_argument("--headless")
    new_session.service = Service(GeckoDriverManager().install())
    new_session.driver = webdriver.Firefox(service=new_session.service, options=options)

    new_session.email = email

    return new_session

def SaveSession(session):
    pass

def LoadSession(session_path):
    pass

#Duolingo
session = NewSession("einarvist@gmail.com")


def LogIn(_session, i):
    _driver = _session.driver
    _driver.get("https://www.duolingo.com/settings/account?isLoggingIn=true")
    sleep(2)
    _driver.refresh()
    sleep(3)
    print("Website grabbed")

    html = _driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    #Chooses sign in
    button = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/button")
    button.click()

    sleep(uniform(1, 1.5))

    #Sets age
    age_number = numpy.random.randint(18, 32)
    age_element = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input")
    # _driver.execute_script("arguments[0].setAttribute('value', arguments[1])", age_element, age_number)
    age_element.click()
    age_element.send_keys(str(age_number))

    sleep(uniform(0.5, 1.5))

    #Sets name
    random_name = randomword(10)
    name_index = numpy.random.randint(0, 4)
    name_element = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/form/div[1]/div[1]/div[2]/label/div/input")
    # _driver.execute_script("arguments[0].setAttribute('value', arguments[1])", name_element, random_name)
    name_element.click()
    name_element.send_keys(random_name)

    sleep(uniform(0.5, 1.5))

    #Sets email
    email_element = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/form/div[1]/div[1]/div[3]/label/div/input")
    # _driver.execute_script("arguments[0].setAttribute('value', arguments[1])", email_element, (_session.email_name + "+" + str(i + 1) + _session.email_service))
    email_element.click()
    email_element.send_keys((_session.email_name + "+" + str(i + 1) + _session.email_service))

    sleep(uniform(0.5, 1.5))

    #Sets password
    password = randomword(10)
    password_element = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/form/div[1]/div[1]/div[4]/label/div/input")
    # _driver.execute_script("arguments[0].setAttribute('value', arguments[1])", password_element, password)
    password_element.click()
    password_element.send_keys(password)

    sleep(uniform(0.5, 1.5))

    #Presses Log In
    log_in_button = _driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/form/div[1]/button")
    log_in_button.click()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(choice(letters) for i in range(length))
