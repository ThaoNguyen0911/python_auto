from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.read_config import ConfigReader
class BasePage:
    def __init__(self, driver):
        self.driver = driver    
        self.timeout = 10
     
    def find_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*locator)
        )
        return element