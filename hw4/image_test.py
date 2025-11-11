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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_image(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='image-container']//img")))

    wait.until(lambda d: len(d.find_elements(By.XPATH, "//div[@id='image-container']//img")) == 4)
    images = driver.find_elements(By.XPATH, "//div[@id='image-container']//img")
    if len(images) < 3:
        raise Exception(f"На странице есть только {len(images)}")

    third_image = images[2]
    alt = third_image.get_attribute("alt")
    assert alt == "award", "Значение атрибута 'alt' не равно 'award'"