from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def add_item_to_cart(self):
        #Нажимаем кнопку Добавить в корзину
        add_button = self.browser.find_element(*CartPageLocators.SUBMIT_BUTTON)
        add_button.click()

    def should_be_info_about_adding(self):
        #Проверяем что элементы присутствуют на странице
        assert self.is_element_present(*CartPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*CartPageLocators.ALERT_TEXT), "Info about adding in cart is abcent"
        #Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*CartPageLocators.ALERT_TEXT).text
        #Проверяем что название товара присутствует в сообщении о добавлении
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*CartPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*CartPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*CartPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.ALERT_TEXT), \
            "Success message is presented, but should not be"

