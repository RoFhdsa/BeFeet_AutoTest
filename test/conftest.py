import pytest
from selenium import webdriver
from DATA.data_connect import URL
from PEGAS.main_page import MainPage

@pytest.fixture()
def drivers():
    """инициализация драйвера Chrome"""
    driver = webdriver.Chrome()
    driver.get(URL().url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(drivers):
    """Предоставляет объект для работы с главной страницей в Chrome."""
    return MainPage(drivers)

@pytest.fixture()
def drivers_ff():
    """инициализация драйвера Firefox"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL.url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page_ff(drivers_ff):
    """Предоставляет объект для работы с главной страницей в Firefox."""
    return MainPage(drivers_ff)