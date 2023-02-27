# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def print_cube(num):
    chrome_options = Options
    chrome_options.unhandled_prompt_behavior = 'dismiss and notify'
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(ChromeDriverManager().install())  # launching browser
    driver.get("https://www.way2automation.com/way2auto_jquery/index.php")  # getting browser url
    driver.maximize_window()  # maximizing browser
    print(driver.name)
    print(driver.title)
    driver.minimize_window()  # minimizing browser
    driver.fullscreen_window()  # full-screen browser size
    driver.quit()  # kill entire session all open windows


def print_square(num):
    chrome_options = Options
    chrome_options.unhandled_prompt_behavior = 'dismiss and notify'
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(ChromeDriverManager().install())  # launching browser
    driver.get("http://seomarketing.logixportfolio.in/")  # getting browser url
    driver.maximize_window()  # maximizing browser
    print(driver.name)
    print(driver.title)
    driver.minimize_window()  # minimizing browser
    driver.fullscreen_window()  # full-screen browser size
    driver.quit()  # kill entire session all open windows


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
