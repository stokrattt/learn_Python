import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from pages.base_page1 import BasePage
from pages.submit_app import LoginPage

class TestExclusive:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)

    def test_exclusive(self):
        self.login_page.open()
        self.login_page.send_info_app()

    def teardown_method(self):
        self.driver.close()
