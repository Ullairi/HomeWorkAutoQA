import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_iframe(driver):
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    text = driver.find_element(By.CSS_SELECTOR, "#content > p:nth-child(2)")
    assert "semper posuere integer et senectus justo curabitur." in text.text

    driver.switch_to.default_content()