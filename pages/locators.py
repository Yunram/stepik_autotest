from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.ID, "login-form")
    REGISTER_FORM_LINK = (By.ID, "register-form")

class CartPageLocators():
    SUBMIT_BUTTON = (By.XPATH, "button.btn-add-to-basket")
    ALERT_TEXT = (By.CLASS_NAME, "alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
