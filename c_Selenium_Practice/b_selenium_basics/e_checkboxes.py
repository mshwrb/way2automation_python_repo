import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

url = "http://www.tizag.com/htmlT/htmlcheckboxes.php"

# common prerequisite
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()

time.sleep(3)
driver.quit()
