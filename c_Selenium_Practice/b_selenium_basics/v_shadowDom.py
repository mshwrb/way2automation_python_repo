import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options.ad
chrome_options.unhandled_prompt_behavior = 'dismiss and notify'
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())  # launching browser
driver.get("https://www.flipkart.com/")  # getting browser url
driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
time.sleep(5)
