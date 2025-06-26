import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
checkbox1 = driver.find_element(By.XPATH, "//input[@id='bmwcheck']")
time.sleep(4)
if not checkbox1.is_selected():
    checkbox1.click()
time.sleep(5)