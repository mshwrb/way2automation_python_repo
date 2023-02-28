import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.rediff.com/"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(1)
explicit_wait = WebDriverWait(driver, 1)
driver.get(url)
driver.fullscreen_window()

pre_signin_locator = "//a[normalize-space()='Sign in']"
next_signin_locator = "//input[@title='Sign in']"

pre_signin = driver.find_element(By.XPATH, pre_signin_locator)
pre_signin.click()
next_signin = driver.find_element(By.XPATH, next_signin_locator)
next_signin.click()

alert = driver.switch_to.alert  # or alert = Alert(driver)

print(alert.text)
time.sleep(3)
alert.accept()
