from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge(executable_path='C:/Selenium/msedgedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.amazon.com/")

search_box = driver.find_element("name", "field-keywords")
search_box.send_keys('hp pavilon Azul')
time.sleep(2)

search_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
search_button.click()
time.sleep(2)

select = driver.find_element(By.PARTIAL_LINK_TEXT, "Portatil 2020 HP Pavilion 15.6")
select.click()
time.sleep(0.5)

drop_select = driver.find_element(By.ID, "quantity")
drop = Select(drop_select)
drop.select_by_value('2')
time.sleep(2)

add_button = driver.find_element(By.ID, "add-to-cart-button")
add_button.click()
time.sleep(2)

cart = driver.find_element(By.ID, "nav-cart-count-container")
cart.click()
time.sleep(1)