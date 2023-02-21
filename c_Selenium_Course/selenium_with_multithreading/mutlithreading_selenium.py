from selenium import webdriver
from threading import Thread

from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

# Define a function to perform some action with Selenium
def perform_action(driver):
    driver.get("https://www.example.com")
    driver.implicitly_wait(5)
    print(driver.title)
    # Add your Selenium code here


# Define a function for each thread
def run_thread(thread_id):
    # Create a new instance of a Selenium driver
    # driver = webdriver.Chrome()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome('chromedriver', options=options)
    # Perform some action with Selenium
    perform_action(driver)
    # Close the driver instance
    driver.quit()


# Define the number of threads to run
num_threads = 5

# Create a list to hold the threads
threads = []

# Create and start each thread
for i in range(num_threads):
    thread = Thread(target=run_thread, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
