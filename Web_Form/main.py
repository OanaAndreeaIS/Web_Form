from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import time

# Install GeckoDriver (automatically downloads the latest version)
driver_path = GeckoDriverManager().install()

# Set up the webdriver with the downloaded GeckoDriver
driver = webdriver.Firefox(service=FirefoxService(executable_path=driver_path))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Așteaptă până când elementul cu id-ul "my-text-id" devine vizibil
text_box = driver.find_element(By.ID, "my-text-id")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

text_box.send_keys("Selector")
time.sleep(5)
submit_button.click()
time.sleep(5)
driver.quit()
