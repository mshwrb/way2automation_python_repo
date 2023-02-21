import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.w3schools.com/"

# common prerequisite
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()

#--------------------------------------Relative Locators--------------------------------------------------



time.sleep(3)