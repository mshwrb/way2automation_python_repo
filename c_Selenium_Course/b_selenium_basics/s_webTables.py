import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.espncricinfo.com/series/sa20-2022-23-1335268/points-table-standings"

# Common Prerequisite
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # deprecated

driver = webdriver.Chrome()
driver.implicitly_wait(5)
explicit_wait = WebDriverWait(driver, 5)
driver.get(url)
driver.maximize_window()

rows = driver.find_elements(By.XPATH, "//tbody/tr")
total_rows = len(rows)

columns = driver.find_elements(By.XPATH, "//tbody/tr[11]/td")
total_columns = len(columns)

print(f"total row count: {total_rows}\ntotal column count in 1 row: {total_columns}")

# for row in rows:
#     print(row.text)

print("---------------second way-------------")
#print(driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[{column}]").text)

for row in range(1, total_rows):
    for column in range(1, total_columns):
        if row % 2 != 0:
            print(driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[{column}]").text,end=" | ")
    print()

time.sleep(3)
