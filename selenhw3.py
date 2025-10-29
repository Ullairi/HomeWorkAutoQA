from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("https://itcareerhub.de/ru")
    driver.maximize_window()
    time.sleep(4)

    pay_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    pay_link.click()
    time.sleep(5)

    driver.save_screenshot("Payment_section.png")
    print("Screenshot saved")

finally:
    driver.quit()