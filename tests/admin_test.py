import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_test import BaseTest
from utils.read_config import ConfigReader
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from time import sleep
class TestAdmin(BaseTest):

    def test_admin(self):
        admin_page = AdminPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.do_login("Admin", "admin123")
        sleep(5)
        admin_page.click_admin_menu()
        admin_text = admin_page.get_admin_text()
        assert admin_text == "Admin"
        admin_page.click_add_btn()
        admin_page.select_user_role()
        admin_page.select_status()
        admin_page.enter_employee_name()
        sleep(5)
        admin_page.enter_user_name()
        admin_page.enter_password()
        admin_page.enter_password_again()
        admin_page.click_btn_save()
        sleep(10)
        admin_page.search_account()
        admin_page.click_search_btn()
        result_txt = admin_page.get_text_result()
        assert result_txt == "(1) Record Found"
       
        
