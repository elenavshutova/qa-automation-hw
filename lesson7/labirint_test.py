from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("python")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    browser.find_element(By.CSS_SELECTOR, ".radioitems-item.view-table").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, "table") )
    )

    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    browser.get("https://www.labirint.ru/cart/")

    txt = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, 'b').text

    assert counter == int(txt)


    sleep(5)

    browser.quit()
test_cart_counter()