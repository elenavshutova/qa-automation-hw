from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pyautogui

def perform_search_test(driver):
    for _ in range(3):
        search_locator = '.btn-primary'
        search_clickable = driver.find_element(By.CSS_SELECTOR, search_locator)
        search_clickable.click()
        print("Клик выполнен")
        pyautogui.press('esc')
        print("Всплывающее окно закрыто")

# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://uitestingplayground.com/classattr")

# Выполнение поиска в Chrome
perform_search_test(chrome_driver)

# Закрытие драйвера Chrome
chrome_driver.quit()

# Инициализация драйвера Firefox
firefox_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://uitestingplayground.com/classattr")

# Выполнение поиска в Firefox
perform_search_test(firefox_driver)

# Закрытие драйвера Firefox
firefox_driver.quit()