from selenium.webdriver.common.by import By
class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def click_checkout_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()