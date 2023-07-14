from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages.MainPage import MainPage
from pages.ResultPage import ResultPage

def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.setup_calculator_waits('45')
    main_page.do_the_calculations()

    result_page = ResultPage(browser)
    result_page.wait_result()
    as_is = result_page.get_result_text()

    assert as_is == '15'

    browser.quit()