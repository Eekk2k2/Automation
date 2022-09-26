from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

#Class for storing country data
class Country:
    name = "" #Name of the country
    CC = "" #Country Code
    ISO1 = "" #Short
    ISO2 = "" #Long
    population = "" #How many people lives there
    areakm2 = "" #How big the country is
    GDP = "" #Income

def GetCountryDataByName(session):
    session.driver.get("https://www.countrycode.org/")
    country = Country()
    country_elements = session.driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr')

    for element in country_elements:
        name_element = element.find_element(By.XPATH, './td[1]/a')
        name = name_element.text
        if name == session.country:
            name_element = element.find_element(By.XPATH, './td[1]/a')
            name = name_element.text

            cc_element = element.find_element(By.XPATH, './td[2]/span')
            cc = cc_element.text

            iso_codes_element = element.find_element(By.XPATH, './td[3]')
            iso1 = iso_codes_element.text.split(' ')[0]
            iso2 = iso_codes_element.text.split(' ')[2]
            
            population_element = element.find_element(By.XPATH, './td[4]')
            population = population_element.text

            areakm2_element = element.find_element(By.XPATH, './td[5]')
            areakm2 = areakm2_element.text

            gpd_element = element.find_element(By.XPATH, './td[6]')
            gpd = gpd_element.text

            country.name = name
            country.CC = cc
            country.ISO1 = iso1
            country.ISO2 = iso2
            country.population = population
            country.areakm2 = areakm2
            country.GDP = gpd
            return country
        else:
            continue

def GetCountryDataByIndex(country_index, driver):
    driver.get("https://www.countrycode.org/")
    country = Country()
    country_elements = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr')
    i = 0
    for element in country_elements:
        if i == country_index:
            name_element = element.find_element(By.XPATH, './td[1]/a')
            name = name_element.text

            cc_element = element.find_element(By.XPATH, './td[2]/span')
            cc = cc_element.text

            iso_codes_element = element.find_element(By.XPATH, './td[3]')
            iso1 = iso_codes_element.split(' ')[0]
            iso2 = iso_codes_element.split(' ')[2]
            
            population_element = element.find_element(By.XPATH, './td[4]')
            population = population_element.text

            areakm2_element = element.find_element(By.XPATH, './td[5]')
            areakm2 = areakm2_element.text

            gpd_element = element.find_element(By.XPATH, './td[6]')
            gpd = gpd_element.text

            country.name = name
            country.CC = cc
            country.ISO1 = iso1
            country.ISO2 = iso2
            country.population = population
            country.areakm2 = areakm2
            country.GDP = gpd
            return country
        elif i > len(country_elements):
            print("Could not find any country by that index, it may be too large")
        else:
            continue
        i += 1