import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.way2automation.com/"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.fullscreen_window()

# Locators
Resources_locator = "//li[@id='menu-item-27617']//span[@class='menu-text'][normalize-space()='Resources']"
Practice_Site_1_locator = "//li[@id='menu-item-27618']//span[@class='menu-text'][normalize-space()='Practice Site 1']"
Selenium_4_pop_up_close_locator = "//i[@class='eicon-close']"

wait = WebDriverWait(driver, timeout=20, poll_frequency=0.01)
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='eicon-close']")))
element_present = wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='eicon-close']")))
print(element_present)

# Elements
Selenium_4_pop_up_close_button = driver.find_element(By.XPATH, Selenium_4_pop_up_close_locator)

# Script
Selenium_4_pop_up_close_button.click()
action = ActionChains(driver)
Resources_menu = driver.find_element(By.XPATH, Resources_locator)
Practice_site_option = driver.find_element(By.XPATH, Practice_Site_1_locator)
action.move_to_element(Resources_menu).perform()
Practice_site_option.click()
time.sleep(3)
driver.quit()
