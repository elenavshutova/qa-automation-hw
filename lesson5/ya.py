from time import sleep
from selenium import webdriver



driver = webdriver.Chrome()


driver.maximize_window()
driver.get("https://vk.com")
sleep(5)
driver.fullscreen_window()
sleep(5)

driver.save_screenshot('./vk.png')


# for x in range(1, 10): туда сюда 10 раз
   # driver.back()
    #driver.forward()
    # driver.refresh() F5

# driver.set_window_size(640, 480)
