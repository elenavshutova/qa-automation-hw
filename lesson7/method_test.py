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

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_labirint():
    browser.get("https://www.labirint.ru")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def switch_to_table():
    browser.find_element(By.CSS_SELECTOR, ".radioitems-item.view-table").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, "table") )
    )

def add_books():
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter

def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")  

def get_cart_counter():
    txt = browser.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]').find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close_driver():
    browser.quit()

def test_cart_counter():
    open_labirint()
    search('python')
    switch_to_table()
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter