from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def autorisation(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def add_item(self):
# Добавление товаров
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item in items:
            self.driver.find_element(By.XPATH,
                        f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button").click()

    def checkout_click(self):
# Оформление заказа
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

# Заполнение данных
    def input_data(self):
        checkout_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "postal-code": "123456"
        }

        for field, value in checkout_data.items():
            self.driver.find_element(By.ID, field).send_keys(value)

        self.driver.find_element(By.ID, "continue").click()

# Проверка суммы
    def get_total(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

