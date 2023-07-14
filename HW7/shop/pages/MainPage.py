from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def autorization(self):
        login = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        login.send_keys("standard_user")
        password = self._driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    