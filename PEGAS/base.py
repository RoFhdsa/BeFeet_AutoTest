import os
import secrets
import string
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def get_all_elements(self, by: By, locator: str, timeout=2) -> WebElement:
        """
        Получить все элементы страницы .

        :param by: вид поиск
        :param locator: Локатор
        :param timeout: время ожидание элемента в сек
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, locator)))

    def click(self,
              by: By, locator: str, timeout=2) -> None:
        """
        Произвести нажатие на элемент

        :param by: вид поиск
        :param locator: Локатор
        :param timeout: время ожидание элемента в сек
        """
        # element = self.driver.find_elements(by, locator)
        # print(f' element = {element.text}')
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        print(f' element = {element.text}')
        self.scroll_page(element)
        element.click()


    def find_element(self, by: By, locator: str) -> None:
        """
        Получить конкретный элементы страницы.

        :param by: вид поиск
        :param locator: Локатор
        """
        return self.driver.find_element(by, locator)

    def find_elements(self, by: By, locator: str) -> None:
        """
        Получить конкретный элементы страницы.

        :param by: вид поиск
        :param locator: Локатор
        """
        return self.driver.find_elements(by, locator)

    def scroll_page(self, element: str) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_blunk (self) -> None:
        action = ActionChains(self.driver)
        action.move_by_offset(0, 0).click().perform()

    def return_actual_url(self):
        return self.driver.current_url

    def create_screenshot(self, name_screenshot: str) -> str:
        alph = string.digits + string.ascii_uppercase
        id = ''.join(secrets.choice(alph) for r in range(32))
        print(f' id = {id}')
        path = f'{self.create_dir()}{os.path.sep}{name_screenshot}{id}.png'
        print(f'path = {path}')
        self.driver.get_screenshot_as_file(path)
        print('создано')
        return path

    @staticmethod
    def create_dir() -> str:
        path = f'logs_files{os.path.sep}{datetime.now().strftime("%Y-%m-%d")}'
        os.makedirs(path, exist_ok=True)
        return path

