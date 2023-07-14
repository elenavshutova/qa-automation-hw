from selenium.webdriver.common.by import By
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_fields(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys('')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro')

    def click_button_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3').click()