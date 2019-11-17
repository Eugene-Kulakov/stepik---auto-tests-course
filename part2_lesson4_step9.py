import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # opening chrome from existing profile
    opt = webdriver.ChromeOptions()
    opt.add_argument('user-data-dir=C:\\Users\\Enya\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\')
    browser = webdriver.Chrome('C:\\Environment\\chromedriver.exe', options=opt)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button_book = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button_book.click()

    input_value = browser.find_element_by_id('input_value')
    result = calc(input_value.text)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(result)
    button = browser.find_element_by_id('solve')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
