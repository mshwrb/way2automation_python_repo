import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "http://www.tizag.com/htmlT/htmlcheckboxes.php"

# common prerequisite
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH, "(//input[@name='sports'])[4]").click()
driver.find_element(By.XPATH, "(//input[@name='sports'])[3]").click()
driver.find_element(By.XPATH, "(//input[@name='sports'])[1]").click()
driver.find_element(By.XPATH, "(//input[@name='sports'])[2]").click()

time.sleep(3)
driver.quit()
