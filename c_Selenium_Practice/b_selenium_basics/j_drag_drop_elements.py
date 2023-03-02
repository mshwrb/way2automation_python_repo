import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://jqueryui.com/resources/demos/droppable/default.html"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.fullscreen_window()

draggable_component_locator = "//div[@id='draggable']"
droppable_component_locator = "//div[@id='droppable']"

droppable_component = driver.find_element(By.XPATH,draggable_component_locator)

ActionChains(driver).drag_and_drop(droppable_component,droppable_component).perform()
time.sleep(3)


