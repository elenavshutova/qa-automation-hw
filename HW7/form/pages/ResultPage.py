from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def check_zip_cod_field(self):
        zip_code_field = self._driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zip_code_color = zip_code_field.value_of_css_property("border-color")
        return zip_code_color
        
    def check_other_fields(self):
        fields = self._driver.find_elements(By.CSS_SELECTOR, '.alert:not(#zip-code)')
        for field in fields:
            field_color = field.value_of_css_property("border-color")
        return field_color