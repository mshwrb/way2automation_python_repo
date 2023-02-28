import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.redbus.in/"
url_1 = "https://www.way2automation.com/"
url_2 = "http://www.tizag.com/htmlT/htmlcheckboxes.php"

chrome_options = webdriver.ChromeOptions()
# chrome_options = Options
chrome_options.headless = True  # headless chrome option
prefs = {"profile.default_content_setting_values.notifications": 2}  # 1 => allow , 2 => block
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url_2)
print(driver.title)
wait = WebDriverWait(driver, timeout=5, poll_frequency=0.01)
element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[4]//input[1]")))
driver.find_element(By.XPATH,"//div[4]//input[1]").click()
driver.find_element(By.XPATH,"//div[4]//input[2]").click()
driver.find_element(By.XPATH,"//div[4]//input[3]").click()
driver.find_element(By.XPATH,"//div[4]//input[4]").click()
time.sleep(5)
