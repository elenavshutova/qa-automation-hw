from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def perform_search_test(driver):
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    last_name.send_keys("Петров")
    adress = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    adress.send_keys("Ленина, 55-3")
    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    phone_number.send_keys("+7985899998787")
    zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
    zip_code.send_keys("")
    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    city.send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    country.send_keys("Россия")
    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    job_position.send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    company.send_keys("SkyPro")



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


perform_search_test(driver)

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-outline-primary mt-3"]').click()


zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
zip_code_class = zip_code_field.get_attribute("class")
assert "alert-danger" in zip_code_class, "Field Zip code is not highlighted in red"
print("Field Zip code is highlighted in red")

fields = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
for field in fields:
    field_id = field.get_attribute("id")
    assert "alert-success" in field.get_attribute("class"), f"Field {field_id} is not highlighted in green"
    print(f"Field {field_id} is highlighted in green")


driver.quit()

