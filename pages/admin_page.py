from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class AdminPage():
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver
        self.get_text = (By.XPATH, "//h6[text()='Dashboard']")
        self.click_admin = (By.XPATH, "//a[@class='oxd-main-menu-item']")
        self.get_admintext = (By.XPATH, "//h6[text()='Admin']")
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    def get_dashboard_text(self):
        get_text = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.get_text)
        )
        return get_text.text
    
    def click_admin_menu(self):
        self.driver.find_element(*self.click_admin).click()
    
    def get_admin_text(self):
        get_admintext = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.get_admintext)
        )
        return get_admintext.text
    def click_add_btn(self):
        add_btn = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.add_btn).click()
        )
        