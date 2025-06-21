from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window
time.sleep(5)
print(driver.title)
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)