from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage():
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_btn = (By.XPATH, "//button")
        self.get_text = (By.XPATH, "//h6[text()='Dashboard']")
        

    def enter_username(self, username:str):
        username_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.username_input)
        )
        username_input.send_keys(username)
    def enter_password(self, password:str):
        password_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.password_input)
        )
        password_input.send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_dashboard_text(self):
        get_text = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.get_text)
        )
        return get_text.text

