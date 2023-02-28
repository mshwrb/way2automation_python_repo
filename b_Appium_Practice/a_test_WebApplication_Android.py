import time

from appium import webdriver

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)

# pass constructor as port number
# get port number from appium gui : eg 4723 , localhost => http://127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(4)
driver.quit()

