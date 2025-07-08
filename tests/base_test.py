import pytest
import requests
from selenium import webdriver
from utils.read_config import ConfigReader

import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
        # This hook is used to capture the outcome of the test
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_call", rep)
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        session = requests.Session()
        request.cls.session = session
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # Initialize the Chrome WebDriver instance
        self.driver = webdriver.Chrome()
        self.driver.get(ConfigReader.get_base_url())
        self.driver.maximize_window()
        request.cls.driver = self.driver
        
        yield
        # Yield to allow tests to run
        

        # if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        #     allure.attach(
        #         self.driver.get_screenshot_as_png(),
        #         name=f"failure_{request.node.name}",
        #         attachment_type=allure.attachment_type.PNG
        #     )
        # # Cleanup after tests
        
        # self.driver.quit()
        try:
            if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=f"failure_{request.node.name}",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
        finally:
            self.driver.quit()