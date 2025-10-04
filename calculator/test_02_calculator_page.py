import pytest
from selenium import webdriver
from calculator.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.enter_delay()
    calculator.click_button()
    calculator.expectation()
    result = calculator.result()
    calculator.close_driver()
    assert result == "15"
