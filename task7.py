from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

#browser = webdriver.Chrome()

#browser.get("http://suninjuly.github.io/wait2.html")

#button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
#button.click()

#message = browser.find_element_by_id("verify_message")

#assert "succesfull" in message.text

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc():
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    num = browser.find_element(By.ID, "input_value")
    x = num.text
    y = calc()

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()


