from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage

def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.fill_fields()
    main_page.click_button_submit()

    result_page = ResultPage(browser)
    as_is_red = result_page.check_zip_cod_field()
    as_is_green = result_page.check_other_fields()

    assert as_is_red == "rgb(245, 194, 199)"
    print("Цвет поля Zip code соответствует ожидаемому красному цвету")

    assert as_is_green == "rgb(186, 219, 204)"
    print("Цвета остальных полей соответствуют ожидаемому зеленому цвету")

    browser.quit()