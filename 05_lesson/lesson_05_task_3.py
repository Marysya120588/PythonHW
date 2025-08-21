from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://the-internet.herokuapp.com/inputs")
search_box = driver.find_element(By.CSS_SELECTOR,"input")
search_box.send_keys("SKY")
search_box.send_keys(Keys.RETURN)
sleep(10)
search_box.clear()
search_box.send_keys("PRO")
search_box.send_keys(Keys.RETURN)
sleep(10)
driver.quit()