from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webelement


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

search_box = driver.find_element(by.name, "field-keywords")
search_box.send_keys("HP Pavilion azul")
