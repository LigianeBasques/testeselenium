from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Program Files\driver\chromedriver.exe")

driver.get('https://www.google.com.br')

print(driver.current_url)
print(driver.title)
print(driver.capabilities['browserVersion'])

element = driver.find_element(By.NAME,"q")
element.click()
element.send_keys("PyJamas Conf")
element.submit()
sleep(3)
assert driver.title == "PyJamas Conf - Pesquisa Google"


driver.close()