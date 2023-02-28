import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.way2automation.com/"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True  # headless mode important for full page screenshots
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)
driver.maximize_window()

path = 'screenshots/fullpage.png'

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot(path)



time.sleep(2)
