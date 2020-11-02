from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link").click()