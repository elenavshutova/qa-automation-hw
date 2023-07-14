from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.ResultPage import ResultPage

def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.autorization()

    products_page = ProductsPage(browser)
    products_page.add_to_cart()
    products_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.click_checkout_button()

    checkout_page = CheckoutPage(browser)
    checkout_page.add_checkout_information()
    checkout_page.click_continue_button()

    result_page = ResultPage(browser)
    as_is = result_page.get_total()

    browser.quit()

    expected_total = "Total: $58.29"
    assert as_is == expected_total
    print("Total value is correct")