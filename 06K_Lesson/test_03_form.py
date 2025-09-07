from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class internet_shop:
    def __init__(self.driver.url:str):
        self._driver = webdriver
        self._driver.get(url)

    def username(self.username.str):
        self._driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)


    def password(self.password.str):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        "https://www.saucedemo.com/")

    def button(self.locator):
        self._driver.find_element(By.CSS_SELECTOR, "locator").click()

    def post(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Мария")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Концевич")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("142411")
    def price(self):
        txt = self._driver.find_element
        (By.CSS_SELECTOR,"summary_total_label").text
        return txt
def test_swag_labs():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
magazine_swag_labs = internet_shop(browser,url = "https://www.saucedemo.com")
magazine_swag_labs.username ("standard_user")
magazine_swag_labs.password_("secret_sauce")
magazine_swag_labs.button("#login_button")

magazine_swag_labs.button('#add-to-cart-sauce-labs-backpack"')
magazine_swag_labs.button('#add-to-cart-sauce-labs-bolt-t-shirt')
magazine_swag_labs.button('#add-to-cart-sauce-onesie')

magazine_swag_labs.button('#shopping_cart_container')
magazine_swag_labs.button('#checkout')

magazine_swag_labs.post()
magazine_swag_labs.button('#continue')

summ = magazine_swag_labs.price()
assert summ == "Total:$58.29"
browser quit()
