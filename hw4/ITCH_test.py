import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://uitestingplayground.com/textinput")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_button(driver):
    wait = WebDriverWait(driver,  5)
    inp_field = driver.find_element(By.ID, "newButtonName")
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))

    inp_field.send_keys("ITCH")
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID,"updatingButton"), "ITCH"))
    assert button.text == "ITCH", "Надпись 'ITCH' не появилась"






