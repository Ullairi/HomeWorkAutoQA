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
    time.sleep(3)
    button_de = driver.find_elements(By.XPATH, '//a[contains(@href,"/de")]')
    button_ru = driver.find_elements(By.XPATH, '//a[contains(@href,"/ru")]')

    assert len(button_de) > 0, "de кнопка не найдена"
    assert len(button_ru) > 0, "ru кнопка не найдена"


def test_phone_button(driver):
    driver.get("https://itcareerhub.de/ru/contact-us")
    time.sleep(3)

    phone_icon = driver.find_element(By.XPATH, '//a[contains(@href,"#popup:form-tr3")]')
    driver.execute_script("arguments[0].click();", phone_icon)
    time.sleep(2)

    text = driver.find_element(By.XPATH, '//div[@class="tn-atom" and contains(text(),"Если вы не дозвонились")]')
    assert text.is_displayed(), "После клика текстт не отображается"