from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_search(driver):
    modal_locator = '#modal'
    close_locator = '#modal .modal-footer p'
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, modal_locator)))
    search_clickable = driver.find_element(By.CSS_SELECTOR, close_locator)
    ActionChains(driver).click(search_clickable).perform()
    print("Окно закрыто")
    sleep(5)

# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/entry_ad")

# Выполнение поиска в Chrome
perform_search(chrome_driver)

# Закрытие драйвера Chrome
chrome_driver.quit()

# Инициализация драйвера Firefox
firefox_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/entry_ad")

# Выполнение поиска в Firefox
perform_search(firefox_driver)

# Закрытие драйвера Firefox
firefox_driver.quit()