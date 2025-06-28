import pytest
from selenium import webdriver
from utils.read_config import ConfigReader

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get(ConfigReader.get_base_url())
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
