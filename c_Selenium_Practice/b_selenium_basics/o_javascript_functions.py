import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onclick"


def capture_ScreenShot(driverRef, path):
    fileName = f"{path}screenshot_{time.asctime().replace(':', '_').replace(' ', '_')}.png"
    driverRef.save_screenshot(fileName)


# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)

driver.switch_to.frame("iframeResult")
# driver.find_element(By.XPATH,"//button[normalize-space()='Click me']").click()
clickMe = driver.find_element(By.XPATH, "//button[normalize-space()='Click me']")
driver.execute_script("arguments[0].style.border='2px solid red'", clickMe)
driver.execute_script("myFunction()")
driver.save_screenshot("./screenshots/error.png")
clickMe.screenshot("./screenshots/element.png")
capture_ScreenShot(driver, "screenshots/")

time.sleep(2)
