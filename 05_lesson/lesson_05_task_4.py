from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")
sleep(10)

login = driver.find_element(By.CSS_SELECTOR,"input#username")
login.send_keys("tomsmith")
sleep(5)

password = driver.find_element(By.CSS_SELECTOR,"input#password")
password.send_keys("SuperSecretPassword!")
sleep(5)

button = driver.find_element(By.CSS_SELECTOR,"button.radius").click()
flash = driver.find_element(By.CSS_SELECTOR, "div#flash")
print(flash.text)

driver.quit()