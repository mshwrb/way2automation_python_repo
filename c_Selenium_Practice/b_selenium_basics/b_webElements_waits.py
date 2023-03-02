"""
<div id="ast-desktop-header" data-toggle-type="dropdown"> <div class="ast-above-header-wrap  ">
or
<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0"
aria-label="Email or phone" name="identifier" value="" autocapitalize="none" id="identifierId" dir="ltr"
data-initial-dir="ltr" data-initial-value="">
#----------------------------------------------------Locators :---------------------------------------------------------
- id  = ast-desktop-header
- name = "......."
- cssSelector = #ast-desktop-header
- xpath = //*[@id="ast-desktop-header"]
- tagName = "div"
- className = "ast-above-header-wrap  "
- linkText = "http......."
- partialLinkText = "....... "

- implicitly_wait(10)  # wait for element to be found or command to complete {check presence of element}
- explicit_wait() # element is present in dom but take while for visible / intractable / clickable on [UI]
sometimes code working on chrome but not working in firefox : throwing ElementNotIntractable exception

difference b/w
                           Implicit wait              |                          Explicit Wait
1. This tied up with browser and for every element    |       1. It can be explicitly implemented on various
   presence it checks for and wait for that time      |          elements until a specific condition is fulfills
                                                      |
2. It should be avoided                               |       2. It is better to use
                                                      |
                                                      |
                                                      |
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.implicitly_wait(5)  # wait for element to be found or command to complete {check presence of element}
explicit_wait = WebDriverWait(driver, 5)

url = "https://www.way2automation.com/"

driver.get(url)
driver.maximize_window()
# dismiss_pop_up
# driver.find_element(By.XPATH, "//*[@id='elementor-popup-modal-26600']/div/div[4]/i").click()
# dismiss_zendesk_pop_up
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]").click()
# click on membership login
driver.find_element(By.XPATH, "//*[@id='menu-item-27625']/a/span[2]").click()
elementPresent = WebDriverWait(driver, timeout=10,poll_frequency=0.25).until(
    EC.presence_of_element_located((By.ID, "remember_me")))  # explicit wait
elementVisible = explicit_wait.until(
    EC.visibility_of_element_located((By.ID, "remember_me")))  # explicit wait
elementClickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elementVisible))  # explicit wait
elementClickable.click()
wait = WebDriverWait(driver, timeout=15, poll_frequency=0.34, ignored_exceptions="")
ele = wait.until(EC.element_to_be_clickable(By.XPATH, "locator"))






# username = driver.find_element("id", "identifierId")
# username = driver.find_element(By.ID, "identifierId")
# username.send_keys("trainer@way2automation.com")
# driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
# password = driver.find_element(By.NAME, "Passwd")
# password.send_keys("asdfg")
# driver.find_element(By.ID, "passwordNext").click()
# error_message = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").text
# print(error_message)
time.sleep(5)
driver.quit()
