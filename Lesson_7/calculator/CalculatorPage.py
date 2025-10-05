from pycparser.ply.yacc import resultlimit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def enter_delay(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def click_button(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def expectation(self):
        WebDriverWait(self.driver, 60).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
            )

    def result(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text

    def close_driver(self):
        self.driver.quit()



