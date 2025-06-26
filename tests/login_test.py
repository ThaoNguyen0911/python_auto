import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        dashboard_text = login_page.get_dashboard_text()
        assert dashboard_text == "Dashboard"

        