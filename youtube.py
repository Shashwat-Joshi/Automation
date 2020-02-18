from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
sleep(2)

search_text = driver.find_element_by_id('search')
search_text.send_keys("Otilia - Adelante (Y3MR$ Remix) alex's list")

search_button = driver.find_element_by_id('search-icon-legacy')
search_button.click()
