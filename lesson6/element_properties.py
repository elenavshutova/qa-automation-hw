from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver.get("https://dzen.ru")

#txt = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').text
#print(txt)

#tag = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').tag_name
#print(tag)

#id = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').id
#print(id)

#href = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').get_attribute("href")
#print(href)

#ff = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').value_of_css_property("font-family")
#print(ff)

#color = driver.find_element(By.CSS_SELECTOR, '[aria-label="Курс USD/RUB"]').value_of_css_property("color")
#print(color)

#driver.get("http://uitestingplayground.com/visibility")
#is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
#print(is_displayed)

#driver.find_element(By.CSS_SELECTOR, '#hideButton').click()
#sleep(2)

#is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
#print(is_displayed)
#sleep(2)

#driver.get("https://demoqa.com/radio-button")
#is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
#print(is_enabled)

#is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
#print(is_enabled)

driver.get("https://the-internet.herokuapp.com/checkboxes")
#cb = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
#is_selected = cb.is_selected()
#print(is_selected)
#cb.click()
#is_selected = cb.is_selected()
#print(is_selected)

#div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

#a = div.find_element(By.CSS_SELECTOR, "a")

#print(a.get_attribute("href"))

divs = driver.find_elements(By.CSS_SELECTOR, "div")
#l = len(divs)
#print(l)

div = divs[6]
css_class = div.get_attribute("class")
print(css_class)

sleep(2)