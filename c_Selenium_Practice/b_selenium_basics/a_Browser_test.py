from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options
chrome_options.unhandled_prompt_behavior = 'dismiss and notify'
driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())  # launching browser
driver.get("https://www.way2automation.com/way2auto_jquery/index.php")  # getting browser url
driver.maximize_window()  # maximizing browser
print(driver.name)
print(driver.title)
driver.minimize_window()  # minimizing browser
driver.fullscreen_window()  # full-screen browser size
driver_options = webdriver.ChromeOptions()
assert "Selenium" in driver.title
driver.quit()  # kill entire session all open windows
# driver.close()  # only kill current window



# driver = webdriver.Firefox()
# driver.get("https://www.way2automation.com/")
# driver.quit()

# driver = webdriver.Safari()
# driver.get("https://www.way2automation.com/")
# driver.fullscreen_window()
# time.sleep(3)



