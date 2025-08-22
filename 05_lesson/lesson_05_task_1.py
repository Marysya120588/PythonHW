from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.fed_cm import click_dialog_button

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

sleep (5)


driver.quit()