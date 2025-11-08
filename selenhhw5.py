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
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    time.sleep(3)
    yield driver
    driver.quit()


def test_logo_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")
    assert logo.is_displayed(), "Логотип 'ITCareerHub' не найден на странице"


def test_programs_link_displayed(driver):
    programs = driver.find_element(By.LINK_TEXT, "Программы")
    assert programs.is_displayed(), "Ссылка 'Программы' не найдена"


def test_payment_methods_link_displayed(driver):
    payments = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert payments.is_displayed(), "Ссылка 'Способы оплаты' не найдена"


def test_about_link_displayed(driver):
    about = driver.find_element(By.LINK_TEXT, "О нас")
    assert about.is_displayed(), "Ссылка 'О нас' не найдена"


def test_reviews_link_displayed(driver):
    reviews = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert reviews.is_displayed(), "Ссылка 'Отзывы' не найдена"

def test_buttons_ru_de(driver):
    button_de = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="/"]')
    driver.execute_script("arguments[0].click();", button_de)
    time.sleep(3)
    assert "itcareerhub.de" in driver.current_url, "После клика на de язык не переключился обратно"

    button_ru = driver.find_element(By.CSS_SELECTOR, 'a.tn-atom[href="/ru"]')
    driver.execute_script("arguments[0].click();", button_ru)
    time.sleep(3)

    assert "/ru" in driver.current_url, "после клика на ru язык не переключился обратно"
    assert "Программы" in driver.page_source, "Страница не вернулась обрано на русский язык"