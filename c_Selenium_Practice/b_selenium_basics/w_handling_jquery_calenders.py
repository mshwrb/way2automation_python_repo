"""
target day, month, year
current day, month, year
jump to the month
increment or decrement
"""
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By


def choose_date_from_jquery_calender(target_date):
    current_date = date.today()
    target_day = int(target_date.split("/")[0])
    target_month = int(target_date.split("/")[1])
    current_month = current_date.month
    increment = True
    if target_month - current_month > 0:
        jump_months_by = target_month - current_month
    else:
        jump_months_by = current_month - target_month
        increment = False
    for i in range(0, jump_months_by):
        if increment:
            driver.find_element(By.XPATH, "//a[@title='Next']").click()
        else:
            driver.find_element(By.XPATH, "//a[@title='Prev']").click()
    driver.find_element(By.LINK_TEXT, str(target_day)).click()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box")
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='example-1-tab-1']//iframe[@class='demo-frame']"))
driver.find_element(By.ID, "datepicker").click()
asdf("16/10/2015")
