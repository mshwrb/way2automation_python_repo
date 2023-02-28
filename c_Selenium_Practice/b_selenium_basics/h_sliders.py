import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://jqueryui.com/resources/demos/slider/default.html"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.fullscreen_window()

# Locators
slider_bar_locator = "//div[@id='slider']"
slider_option_locator = "//span[@class='ui-slider-handle ui-corner-all ui-state-default']"

slider_bar = driver.find_element(By.XPATH,slider_bar_locator)
slider_option = driver.find_element(By.XPATH,slider_option_locator)

# ActionChains(driver).drag_and_drop_by_offset(slider_option,400,0).perform()

location = slider_bar.location
size = slider_bar.size
print(location)
print(size.items())
width,height = size["width"],size["height"]

ActionChains(driver).drag_and_drop_by_offset(slider_option,width/2,0).perform()
time.sleep(3)


