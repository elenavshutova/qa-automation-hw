from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def perform_search(driver):
    search_locator_username = '#username'
    search_field = driver.find_element(By.CSS_SELECTOR, search_locator_username)
    search_field.send_keys("tomsmith")
    print("Логин введен")
    sleep(2)
    search_locator_username = '#password'
    search_field = driver.find_element(By.CSS_SELECTOR, search_locator_username)
    search_field.send_keys("SuperSecretPassword!")
    print("Пароль введен")
    sleep(2)
    search_locator = '[class="fa fa-2x fa-sign-in"]'
    search_clickable = driver.find_element(By.CSS_SELECTOR, search_locator)
    ActionChains(driver).click(search_clickable).perform()
    print("Клик выполнен")
    sleep(5)



# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/login")

# Выполнение поиска в Chrome
perform_search(chrome_driver)

# Закрытие драйвера Chrome
chrome_driver.quit()

# Инициализация драйвера Firefox
firefox_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/login")

# Выполнение поиска в Firefox
perform_search(firefox_driver)

# Закрытие драйвера Firefox
firefox_driver.quit()