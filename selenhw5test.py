import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://itcareerhub.de/ru/contact-us")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()


def test_phone_button(driver):
    phone_icon = driver.find_element(By.CSS_SELECTOR, 'a[href*="#popup:form-tr3"]')
    driver.execute_script("arguments[0].click();", phone_icon)
    time.sleep(3)

    text = driver.find_element(By.XPATH, '//div[@class="tn-atom" and contains(text(),"Если вы не дозвонились")]')
    assert text.is_displayed(), "После клика текст не отображается"