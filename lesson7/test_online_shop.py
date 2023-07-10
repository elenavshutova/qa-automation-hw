from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#авторизация
login = driver.find_element(By.CSS_SELECTOR, '#user-name')
login.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("secret_sauce")
login_button = driver.find_element(By.CSS_SELECTOR, '#login-button').click()

#добавление в корзину
backpack = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
shirt = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
onesie = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

#переход в корзину
cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

#Нажмите Checkout
checkout_button = driver.find_element(By.CSS_SELECTOR, '#checkout').click()

#заполнить данные
first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys("Elena")
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys("Shutova")
zip_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip_code.send_keys("640026")

#Нажмите кнопку Continue
continue_button = driver.find_element(By.CSS_SELECTOR, '#continue').click()

#прочитать итоговую стоимость
total_element = driver.find_element(By.CSS_SELECTOR, '.summary_info_label.summary_total_label')
total_text = total_element.text

print("Total value:", total_text)


driver.quit()

#проверка итоговой суммы
expected_total = "Total: $58.29"
assert total_text == expected_total, f"Unexpected total. Expected: {expected_total}, Actual: {total_text}"
print("Total value is correct")