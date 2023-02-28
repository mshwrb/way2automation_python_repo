import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.way2automation.com/"

# common prerequisite
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()


def isElementPresent(id):
    try:
        driver.find_element(By.ID, id)
        return True
    except NoSuchElementException:
        return False


Member_Login = driver.find_element(By.XPATH, "//*[@id='menu-item-27625']/a/span[2]")
Member_Login.click()
Remember_me_checkbox = driver.find_element(By.ID, "remember_me")
Remember_me_checkbox.click()
# email = driver.find_element(By.ID, "email")
# email.clear()
# password = driver.find_element(By.ID,"password")
# password.clear()
"""
LogIn_btn = driver.find_element(By.NAME, "commit")
LogIn_btn_display_status = LogIn_btn.is_displayed()
print(LogIn_btn_display_status)
"""
#LogIn_btn = driver.find_element(By.NAME, "commit23456")
isElementPresent("commit")



time.sleep(2)
