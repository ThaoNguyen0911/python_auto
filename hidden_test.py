import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

hide_button = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
hide_button.click()
time.sleep(5)
displayed_textbox = driver.find_element(By.XPATH, "//input[@name='show-hide']")
driver.execute_script("arguments[0].value ='Hello Thao Nguyen'", displayed_textbox)
time.sleep(5)
show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']").click()
# show_button.click()
time.sleep(5)
displayed_textbox.clear()
time.sleep(5)