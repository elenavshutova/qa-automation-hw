from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_assert_total_value():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    login = driver.find_element(By.CSS_SELECTOR, '#user-name')
    login.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    # Добавление в корзину
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    # Переход в корзину
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    # Нажатие на Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    # Заполнение данных
    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.send_keys("Elena")
    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.send_keys("Shutova")
    zip_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    zip_code.send_keys("640026")

    # Нажатие на кнопку Continue
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Чтение итоговой стоимости
    total_element = driver.find_element(By.CSS_SELECTOR, '.summary_info_label.summary_total_label')
    total_text = total_element.text

    print("Total value:", total_text)

    # Закрытие браузера
    driver.quit()

    # Проверка итоговой суммы
    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Unexpected total. Expected: {expected_total}, Actual: {total_text}"
    print("Total value is correct")

test_assert_total_value()
