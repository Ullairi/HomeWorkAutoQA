import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()

def test_dragdrop(driver):
    wait = WebDriverWait(driver, 15)
    try:
        consent_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button")))
        consent_button.click()
    except:
        pass

    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))))

    source = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gallery > li:nth-child(1)")))
    target = wait.until(EC.element_to_be_clickable((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#trash ul > li")))

    trash = driver.find_elements(By.CSS_SELECTOR, "#trash ul > li")
    images = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")

    assert len(trash) == 1, "в корзине должна быть 1 картинка"
    assert len(images) == 3, "в галерее должно быть 3 картины"

    driver.switch_to.default_content()