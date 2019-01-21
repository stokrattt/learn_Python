import allure
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    EXC_BUTTON = (By.CSS_SELECTOR, "div[datatest='providers_form_inspect_connect_tariff_button']")
    PHONE_INPUT = (By.XPATH, "//input[class='app554']")
    NAME_INPUT = (By.XPATH, "//span[contains(text(), 'Ваше имя')]")
    EMAIL_INPUT = (By.XPATH, "//span[contains(text(), 'Ваш E-mail')]")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div[datatest='registration_button_register']")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def send_info_app(self):
        self.driver.find_element(*self.EXC_BUTTON).click()
        self.driver.implicitly_wait(5)

        self.driver.find_element(*self.PHONE_INPUT).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.PHONE_INPUT).send_keys("1111111111")
        self.driver.find_element(*self.NEXT_BUTTON).click()
        self.driver.find_element(*self.NAME_INPUT).send_keys("test_REVUE-AUTO-TEST")
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("test@test.REVUEAUTOTEST")
        self.driver.find_element(*self.NEXT_BUTTON).click()
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*self.NEXT_BUTTON)).click()
 
    @allure.step
    def open(self):
        self.driver.get("https://piter-online.net")
        return self
