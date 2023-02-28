import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "http://www.dummysoftware.com/popupdummy_testpage.html"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated
driver = webdriver.Chrome()
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)
#driver.fullscreen_window()
popup_generator = driver.find_element(By.XPATH,"//input[@name='mouseoverpopup']")
ActionChains(driver).move_to_element(popup_generator).perform()
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
print(driver.window_handles)

while len(driver.window_handles) > 2:
    driver.switch_to.window(driver.window_handles[2])
    driver.close()

driver.switch_to.window(driver.window_handles[1])

driver.forward()
driver.get_log("log_type")
driver.get_sinks()
driver.get_cookies()
driver.get_screenshot_as_png()
driver.get_pinned_scripts()
driver.get_screenshot_as_base64()
driver.get_credentials
driver.get_issue_message()
driver.get_network_conditions()
driver.get_window_size()
driver.get_window_rect()
driver.get_window_position()
driver.get_cookie("cookie_name")

driver.set_window_rect(x="",y="",width="",height="")
driver.set_window_position(x="",y="",windowHandle="")
driver.set_window_size(width="",height="",windowHandle="")
driver.set_permissions(name="",value="")
driver.set_sink_to_use(sink_name="")
driver.set_page_load_timeout(time_to_wait=23.43)
driver.set_script_timeout(time_to_wait=23.345)
driver.implicitly_wait()
driver.find_element(By.XPATH,"//font[normalize-space()='PopupDummy!']")
time.sleep(5)



