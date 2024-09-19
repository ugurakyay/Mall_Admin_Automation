import pytest
import allure
from pages.login_page import LoginPage
from utils.driver import get_driver
from config.settings import BASE_URL, USERNAME, PASSWORD

@allure.feature('Login Feature')
class TestLogin:
    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.story('Successful Login')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        with allure.step("Entering username"):
            self.login_page.enter_username(USERNAME)
        with allure.step("Entering password"):
            self.login_page.enter_password(PASSWORD)
        with allure.step("Clicking checkbox"):
            self.login_page.click_checkbox()
        with allure.step("Clicking pop-up confirmation button"):
            self.login_page.click_popup_button()
        with allure.step("Clicking login button"):
            self.login_page.click_login()
        with allure.step("Verifying login success"):
            assert "Mall Logistics Panel" in self.driver.title

if __name__ == "__main__":
    pytest.main()
