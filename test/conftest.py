import pytest
from selenium import webdriver
from DATA.data_connect import URL
from PEGAS.main_page import MainPage

@pytest.fixture()
def drivers():
    """инициализация драйвера"""
    driver = webdriver.Chrome()
    driver.get(URL.url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(drivers):
    """Предоставляет объект для работы с главной страницей."""
    return MainPage(drivers)

