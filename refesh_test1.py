from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
print(f'\nTitle web: {driver.title}')

# Refresh the page
driver.refresh()
time.sleep(3)  # Wait to observe the refresh
print(f'Title web: {driver.title}')
driver.close()