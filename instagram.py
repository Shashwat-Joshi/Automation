from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = driver.find_element_by_name('username')
username.send_keys('your_username')                  #enter your username

password = driver.find_element_by_name('password')
password.send_keys('your_password')                  #enter your password
password.submit()
