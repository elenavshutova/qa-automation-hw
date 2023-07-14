from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def get_total(self):
        total_element = self._driver.find_element(By.CSS_SELECTOR, '.summary_info_label.summary_total_label')
        total_text = total_element.text
        print("Total value:", total_text)
        return total_text