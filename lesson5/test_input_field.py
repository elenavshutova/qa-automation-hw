from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def perform_search(driver):
    search_locator = '[type="number"]'
    search_field = driver.find_element(By.CSS_SELECTOR, search_locator)
    search_field.send_keys("1000")
    print("Значение введено в поле ввода")
    search_field.clear()
    print("Поле очищено")
    search_field.send_keys("999")
    print("Значение в поле ввода изменено")

# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/inputs")

# Выполнение поиска в Chrome
perform_search(chrome_driver)

# Закрытие драйвера Chrome
chrome_driver.quit()

# Инициализация драйвера Firefox
firefox_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/inputs")

# Выполнение поиска в Firefox
perform_search(firefox_driver)

# Закрытие драйвера Firefox
firefox_driver.quit()