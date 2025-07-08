from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .login_page import LoginPage
from utils.read_config import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
import time
class AdminPage():
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver
        self.user_data = ConfigReader.new_user()

        self.get_text = (By.XPATH, "//h6[text()='Dashboard']")
        self.click_admin = (By.XPATH, "//a[@class='oxd-main-menu-item']")
        self.get_admintext = (By.XPATH, "//h6[text()='Admin']")
        #add user
        self.add_btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.user_role = (By.XPATH, "//div[@class='oxd-select-text-input']")
        self.user_dropdown = (By.XPATH, "//div[@role='listbox' and @loading='false']")
        self.status = (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-text-input']")
        self.status_dropdown = (By.XPATH, "//div[@role='listbox' and @loading='false']")
        self.employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_dropdown = (By.XPATH, "//div[@role='listbox']")
        self.username_add = (By. XPATH, "//label[text()='Username']/following::input[1]")
        self.password_add = (By.XPATH, "//label[text()='Password']/following::input[1]")
        self.password_again = (By.XPATH, "//label[text()='Password']/following::input[2]")
        self.save_btn = (By.XPATH, "//button[@type ='submit']")
        #search user
        self.user_search = (By.XPATH, "//label[text()='Username']/following::input[1]")
        self.search_btn = (By.XPATH, "//button[@type='submit']")
        self.result = (By.XPATH, "//span[text()='(1) Record Found']")


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
        self.driver.find_element(*self.add_btn).click()

    
    def select_user_role(self):
        role = self.user_data["user_role"]
    # Mở dropdown trước
        dropdown_user = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.user_role)
        )
        dropdown_user.click()

        # Chờ dropdown render xong và chọn option "Admin"
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.user_dropdown)
        )

        dropdown_element = self.driver.switch_to.active_element
        for _ in range(10):  # thử tối đa 10 lần
            dropdown_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(2)  # đợi UI cập nhật
            selected = self.driver.find_element(*self.user_role).text
            if selected.strip() == role:
                dropdown_element.send_keys(Keys.ENTER)
                return
        raise Exception("❌ Không tìm thấy lựa chọn 'Admin' trong dropdown")
    
    def select_status(self):
        status = self.user_data["status"]
    # Mở dropdown trước
        dropdown_status = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.status)
        )
        dropdown_status.click()

        # Chờ dropdown render xong và chọn option "Admin"
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.status_dropdown)
        )

        dropdown_element = self.driver.switch_to.active_element
        for _ in range(10):  # thử tối đa 10 lần
            dropdown_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)  # đợi UI cập nhật
            selected = self.driver.find_element(*self.status).text
            if selected.strip() == status:
                dropdown_element.send_keys(Keys.ENTER)
                return
        raise Exception("❌ Không tìm thấy lựa chọn 'Enabled' trong dropdown")
    
    def enter_employee_name(self):
        employee_name = self.user_data["employee_name"]
        enter_name = WebDriverWait(self.driver, self.timeout).until (
            lambda d: d.find_element(*self.employee_name)
        )
        enter_name.click()
        
        enter_name.send_keys(employee_name)
        time.sleep(1.5)
        # Mô phỏng người dùng nhấn ↓ và Enter
        actions = ActionChains(self.driver)
        actions.move_to_element(enter_name)
        actions.click()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    def enter_user_name(self):
        user_name = self.user_data["username_add"]
        enter_username = WebDriverWait(self.driver, self.timeout).until (
            lambda d: d.find_element(*self.username_add)
        )
        enter_username.send_keys(user_name)


    def enter_password(self):
        password = self.user_data["password_add"]
        enter_password = WebDriverWait(self.driver, self.timeout).until (
            lambda d: d.find_element(*self.password_add)
        )
        enter_password.send_keys(password)

    def enter_password_again(self):
        password_again = self.user_data["password_add_again"]
        confirm_password = WebDriverWait(self.driver, self.timeout).until (
            lambda d: d.find_element(*self.password_again)
        )
        confirm_password.send_keys(password_again)

    def click_btn_save(self):
        self.driver.find_element(*self.save_btn).click()

    def search_account(self):
        account_name = self.user_data["username_add"]   
        enter_account = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.user_search)
        )
        enter_account.send_keys(account_name)   
    
    def click_search_btn(self):
        search_btn =WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.search_btn)
        )
        search_btn.click()

    def get_text_result(self):
        result_text = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.result)
        )
        return result_text.text