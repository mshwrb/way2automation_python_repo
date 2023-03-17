import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.implicitly_wait(10)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//span[normalize-space()='Account & Lists']")).perform()
driver.find_element(By.XPATH, "//div[@id='nav-flyout-ya-newCust']//a[@class='nav-a'][normalize-space()='Start here.']").click()
time.sleep(5)


payload = open(r"jsonfile").read()

payload.propertyname[0]

