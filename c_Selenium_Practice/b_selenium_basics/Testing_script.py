import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://seomarketing.logixportfolio.in/")  # getting browser url
driver.maximize_window()  # maximizing browser
driver.find_element(By.ID, "txtEmailid").send_keys(" sandeep.agarwal@khamelia.net")
time.sleep(1)
driver.find_element(By.ID, "txtPassword").send_keys("Pass@13")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.01)
element_present = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[text()='Invalid User Name and Password!']")))
element_present_visible = wait.until(
    EC.visibility_of(element_present))
status = driver.find_element(By.XPATH, "//div[text()='Invalid User Name and Password!']").is_displayed()
print(status)

