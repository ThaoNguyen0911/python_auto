
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_test import BaseTest
from pages.login_page import LoginPage
from utils.read_config import ConfigReader
import allure
class TestLogin(BaseTest):
    @allure.story("Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        login_page = LoginPage(self.driver)
        username = ConfigReader.get_username()
        password = ConfigReader.get_password()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        dashboard_text = login_page.get_dashboard_text()
        assert dashboard_text == "Dashboard"

        