from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def setup_calculator_waits(self, term):
        input_number = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        input_number.clear()
        input_number.send_keys(term)

    def do_the_calculations(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        equal_button = self._driver.find_element(By.XPATH, "//span[text()='=']")
        equal_button.click()