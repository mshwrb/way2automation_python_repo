import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

url = "https://jqueryui.com/dialog/"
url_1 = "https://jqueryui.com"
url_2 = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_submit"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url_2)
driver.fullscreen_window()
test_element = driver.find_element(By.XPATH, "//input[@value='Submit']")
select = Select(test_element)
driver.switch_to.frame('iframeResult')  # we must take id/name of iframe
# driver.find_element(By.XPATH,"//button[normalize-space()='Close']").click() # url and url_1
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

driver.switch_to.default_content()  # bring back focus to current screen

frames = driver.find_elements(By.TAG_NAME, "iframe")
for frame in frames:
    print(frame.get_attribute(By.ID))
print(len(frames))

time.sleep(2)
