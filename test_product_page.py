import time
import pytest
from .pages.product_page import CartPage


#def test_guest_can_add_product_to_basket(browser, promo):
 #   #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
 #   #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
  #  link = promo
  #  page = CartPage(browser, link)
  #  page.open()
  #  page.add_item_to_cart()
   # page.should_be_info_about_adding()
   # page.should_be_message_basket_total()
@pytest.mark.parametrize('promo', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo):
    link = promo
    page = CartPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()

@pytest.mark.parametrize('promo', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, promo):
    link = promo
    page = CartPage(browser, link)
    page.open()
    page.should_not_be_success_message()