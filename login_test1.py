from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button").click()
time.sleep(3)
get_text = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
assert get_text.text == "Dashboard"
time.sleep(5)

