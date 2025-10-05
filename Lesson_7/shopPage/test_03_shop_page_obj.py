import pytest
from selenium import webdriver
from Lesson_7.shopPage.ShopPage import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_total(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.autorisation()
    shop_page.add_item()
    shop_page.checkout_click()
    shop_page.input_data()
    total = shop_page.get_total()
    assert total == "Total: $58.29"





