from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('C:/Users/Samue/Downloads/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
element = driver.find_element(By.ID, "twotabsearchtextbox")
element.send_keys("HP Pavilion azul")
button_search = driver.find_element(By.ID, "nav-search-submit-button")
button_search.click()
option = driver.find_element(By.LINK_TEXT, "HP Portátil con pantalla táctil FHD de 15.6 pulgadas, 11ª generación Core i7-1165G7, WiFi-6, teclado retroiluminado, USB-C, HDMI, gráficos Iris Xe, 16 GB RAM, SSD PCIe de 512 GB, Win 10, azul niebla")
option.click()

cant1 = driver.find_element(By.ID, "a-autoid-0")
cant1.click()
cant2 = driver.find_element(By.XPATH, '//*[@id="quantity_1"]')
cant2.click()
car = driver.find_element(By.ID, 'add-to-cart-button')
car.click()
car2 = driver.find_element(By.ID, 'sw-gtc')
car2.click()

time.sleep(5000)
driver.quit()
