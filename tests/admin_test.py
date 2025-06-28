import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_test import BaseTest
from utils.read_config import ConfigReader
from pages.admin_page import AdminPage
from .login_test import TestLogin
class TestAdmin(TestLogin):
    def test_admin(self):
        admin_page = AdminPage(self.driver)

        admin_page.click_admin_menu()
        admin_text = admin_page.get_admin_text()
        assert admin_text == "Admin"
        admin_page.click_add_btn()
        
