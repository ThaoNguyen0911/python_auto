import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest
import time
class LoginTest(BaseTest):
    def test_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button").click()
        time.sleep(3)
        get_text = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        assert get_text.text == "Dashboard"