from selenium.webdriver.common.by import By
class CheckoutPage:

    def __init__(self, browser):
        self._driver = browser

    def add_checkout_information(self):
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.send_keys("Elena")
        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.send_keys("Shutova")
        zip_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        zip_code.send_keys("640026")

    def click_continue_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()