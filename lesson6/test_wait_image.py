from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки всех картинок
wait = WebDriverWait(driver, 40)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(4)")))

# Получение значения атрибута src у 3-й картинки
third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")
third_image_src = third_image.get_attribute("src")

# Вывод значения в консоль
print(third_image_src)


driver.quit()