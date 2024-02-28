import os
import secrets
import string
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def get_all_elements(self,
                         by: By,
                         locator: str,
                         timeout=10
                         ) -> WebElement:
        """
        Получить все элементы страницы .

        :param by: вид поиск
        :param locator: Локатор
        :param timeout: время ожидание элемента в сек
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, locator)))

    def click(self,
              by: By,
              locator: str,
              timeout=5
              ) -> None:
        """
        Произвести нажатие на элемент

        :param by: вид поиск
        :param locator: Локатор
        :param timeout: время ожидание элемента в сек
        """
        # element = self.driver.find_elements(by, locator)
        # print(f' element = {element.text}')
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def find_element(self, by: By,
                     locator: str
                      ) -> None:
        """
        Получить конкретный элементы страницы.

        :param by: вид поиск
        :param locator: Локатор
        """
        return self.driver.find_element(by, locator)

    def find_elements(self, by: By,
                     locator: str
                      ) -> None:
        """
        Получить конкретный элементы страницы.

        :param by: вид поиск
        :param locator: Локатор
        """
        return self.driver.find_elements(by, locator)


    def return_actual_url(self):
        return self.driver.current_url

    def create_screenshot(self, name_screenshot: str) -> str:
        alph = string.digits + string.ascii_uppercase
        id = ''.join(secrets.choice(alph) for r in range(32))
        path = f'{self.create_dir()}{os.path.sep}{name_screenshot}{id}.png'
        self.driver.get_screenshot_as_file(path)
        return path

    @staticmethod
    def create_dir() -> str:
        path = f'logs_files{os.path.sep}{datetime.now().strftime("%Y-%m-%d")}'
        os.makedirs(path, exist_ok=True)
