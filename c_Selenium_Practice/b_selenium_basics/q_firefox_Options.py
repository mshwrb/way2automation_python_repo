import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.google.com/"

firefox_options = webdriver.FirefoxOptions()
#fireox_options = Options
firefox_options.headless = True

firefox_options.set_preference("dom.webnotification.enabled",False)

driver = webdriver.Firefox(options=firefox_options)
# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)
print(driver.title)
time.sleep(5)
