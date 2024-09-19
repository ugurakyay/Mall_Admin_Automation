import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'email')
        self.password_input = (By.ID, 'password')
        self.checkbox = (By.XPATH, "//label[contains(text(), 'Aydınlatma Metni')]")
        self.popup_button = (By.XPATH, "//button[contains(text(), 'Okudum, Anladım, Onaylıyorum')]")
        self.login_button = (By.ID, ':r2:')  # Giriş butonu ID'si

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        time.sleep(2)  # Her adım sonrası 5 saniye bekleme

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        time.sleep(2)

    def click_checkbox(self):
        self.driver.find_element(*self.checkbox).click()
        time.sleep(5)

    def click_popup_button(self):
        # Pop-up butonunu bul ve üzerine mouse over yaparak tıkla
        wait = WebDriverWait(self.driver, 10)
        popup_button_element = wait.until(EC.element_to_be_clickable(self.popup_button))

        # Mouse over yap ve tıkla
        actions = ActionChains(self.driver)
        actions.move_to_element(popup_button_element).click().perform()
        time.sleep(2)

    def click_login(self):
        # Login butonuna tıklamadan önce elementin tıklanabilir olmasını bekle
        wait = WebDriverWait(self.driver, 10)
        login_button_element = wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()
        time.sleep(5)
