import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_iframe(driver):
    wait = WebDriverWait(driver, 10)
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe"))))

    text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > p:nth-child(2)")))
    assert "semper posuere integer et senectus justo curabitur." in text.text

    driver.switch_to.default_content()