import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://jqueryui.com/resources/demos/resizable/default.html"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.fullscreen_window()

resizable_component_locator = "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']"

resizable_component = driver.find_element(By.XPATH,resizable_component_locator)

ActionChains(driver).drag_and_drop_by_offset(resizable_component,400,400).perform()
time.sleep(3)


