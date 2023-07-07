from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

element = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
element.clear()
element.send_keys("test skypro")
sleep(3)
element = driver.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()

sleep(10)

driver.quit()
