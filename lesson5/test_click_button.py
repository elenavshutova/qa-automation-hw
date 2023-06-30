from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def perform_search_test(driver):
    for _ in range(5):
        search_locator = '[onclick="addElement()"]'
        search_clickable = driver.find_element(By.CSS_SELECTOR, search_locator)
        ActionChains(driver).click(search_clickable).perform()

#seconds_to_work = 1.3  # Сколько выполнять цикл, в секундах
#start = time()  # время начала выполнения
#while time() - start < seconds_to_work: Это для меня комментарий, пример как настроить цикл по времени

    delete_button = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    count = len(delete_button)
    print("There are", count, "elements")

# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Выполнение поиска в Chrome
perform_search_test(chrome_driver)

# Закрытие драйвера Chrome
chrome_driver.quit()

# Инициализация драйвера Firefox
firefox_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Выполнение поиска в Firefox
perform_search_test(firefox_driver)

# Закрытие драйвера Firefox
firefox_driver.quit()