from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_number = driver.find_element(By.CSS_SELECTOR, '#delay')
input_number.clear()
input_number.send_keys("45")

buttons = driver.find_elements(By.CSS_SELECTOR, '.keys .btn')
for button in buttons:
    button_text = button.text
    if button_text == '7':
        button.click()
    elif button_text == '+':
        # Нажимаем кнопку "+"
        operator_button = button
        operator_button.click()
        break  # Прерываем цикл после нажатия кнопки "+"

# Нажатие на кнопку 8
for button in buttons:
    button_text = button.text
    if button_text == '8':
        button.click()

# Нажатие на кнопку =
equal_button = driver.find_element(By.CSS_SELECTOR, '.keys .btn.btn-outline-warning')
equal_button.click()


# Ожидание результата в течение 45 секунд
WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

# Получение текста результата
result_element = driver.find_element(By.CSS_SELECTOR, '.screen')
result = result_element.text

# Проверка результата
expected_result = '15'
assert result == expected_result, f"Unexpected result. Expected: {expected_result}, Actual: {result}"
print(f"Result is correct: {result}")

driver.quit()
