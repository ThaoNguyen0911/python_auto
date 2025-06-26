import pytest
from selenium import webdriver
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
