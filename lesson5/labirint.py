from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.maximize_window()
driver.get("https://www.labirint.ru")

search_locator = "#search-field"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("Python", Keys.RETURN)

books = driver.find_elements(By.CSS_SELECTOR, "div.product")

for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'span.product-title').text
    price = book.find_element(By.CSS_SELECTOR, 'span.price-val').text
    
    autor = ''
    try:
        autor = book.find_element(By.CSS_SELECTOR, 'div.product-author').text
    except:
        autor = "Автор не указан"



    print(autor + "\t" + title + "\t" + price)

sleep(5)
