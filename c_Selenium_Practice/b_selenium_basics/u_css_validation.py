from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.w3schools.com/"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated

driver = webdriver.Chrome()
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)
driver.maximize_window()

login_button = driver.find_element(By.ID, "w3loginbtn")
print(login_button.value_of_css_property("font-size"))
print(login_button.value_of_css_property("background-color"))
print(login_button.value_of_css_property("vertical-align"))
print(login_button.value_of_css_property("font-family"))
print(login_button.value_of_css_property("float"))
