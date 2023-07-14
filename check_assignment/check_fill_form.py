from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_fill_form():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    # Открытие страницы
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys('')
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro')

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3').click()

    red_color = "rgb(245, 194, 199)"  # Эталонный красный цвет
    green_color = "rgb(186, 219, 204)"  # Эталонный зеленый цвет

    # Проверка поля Zip code (красный цвет)
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    zip_code_color = zip_code_field.value_of_css_property("border-color")
    assert zip_code_color == red_color, "Цвет поля Zip code не соответствует ожидаемому красному цвету"
    print("Цвет поля Zip code соответствует ожидаемому красному цвету")

    fields = driver.find_elements(By.CSS_SELECTOR, '.alert:not(#zip-code)')
    for field in fields:
        field_color = field.value_of_css_property("border-color")
        assert field_color == green_color, "Цвет поля не соответствует ожидаемому зеленому цвету"
    print("Цвета остальных полей соответствуют ожидаемому зеленому цвету")


    # Закрытие веб-драйвера
    driver.quit()


# Запуск теста
test_fill_form()
