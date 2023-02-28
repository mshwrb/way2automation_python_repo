import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://deluxe-menu.com/popup-mode-sample.html"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.fullscreen_window()

right_click_image_locator = "//img[@src='data-samples/images/popup_pic.gif']"
right_click_image = driver.find_element(By.XPATH,right_click_image_locator)

ActionChains(driver).context_click(right_click_image).perform()
time.sleep(3)




