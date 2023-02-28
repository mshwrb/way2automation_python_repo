import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.wikipedia.org/"

# common prerequisite
driver = webdriver.Chrome()
driver.implicitly_wait(10)
explicit_wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()

"""
# it's not 100% accurate
# for [selecting values]/[typing] we use sendkeys
# url: https://echoecho.com/sampledropdown.htm
driver.find_element(By.XPATH, "/html/body/form[1]/select").send_keys("HOTBOT")
"""

# Another way
"""
dropdown = driver.find_element(By.ID, "searchLanguage")
select = Select(dropdown)
select.select_by_value("pl")
select.select_by_visible_text("Azərbaycanca")
select.select_by_index(7)
select.select_by_visible_text("العربية")
"""
# language drop-down and there respective option
"""
options = dropdown.find_elements(By.TAG_NAME, "option")
for option in options:
    language = option.get_attribute("lang")
    print(f"Text is: {option.text} and language is: {language}")

print(f"Total options in list are {len(options)}")
"""

# links text , their count and url
otherProject = driver.find_element(By.CLASS_NAME, "other-projects")
# otherProjectsLinks = otherProject.find_elements(By.CLASS_NAME, "other-project-link")
# otherProjectsTitles = otherProject.find_elements(By.CLASS_NAME, "other-project-title jsl10n")
# otherProjectsTagline = otherProject.find_elements(By.CLASS_NAME, "other-project-tagline jsl10n")

"""
links = driver.find_elements(By.TAG_NAME, "a")
print("total links: ", len(links))
for link in links:
    print("link url is : ", link.get_attribute("href"))
    print("link text is: ", link.text)
"""

otherProjects_Block = driver.find_element(By.CLASS_NAME, "other-projects")
otherProjects_Block_links = otherProjects_Block.find_elements(By.TAG_NAME, "a")

"""
print("total links: ", len(otherProjects_Block_links))
for link in otherProjects_Block_links:
    print("link url is : ", link.get_attribute("href"))
    print("link text is: ", link.text)
"""
# getting first link from the links :
print("first item in the list is: ",otherProjects_Block_links.__getitem__(0).text)

time.sleep(10)
