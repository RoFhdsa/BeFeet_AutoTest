import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from PEGAS.base import Base


class Mediator(Base):

    def check_element (self, d_locator:dict, element: str) -> True or TimeoutException:
        """ проверить существование элемента """
        try:
            by, locator = self.type_find(d_locator, element)
            elements = self.get_all_elements(by, locator)
            self.scroll_page(elements[0])
            return True
        except TimeoutException:
            return False

    def type_find(self, d_locator: dict, element:str) -> By and str or ValueError:
        """ определить тип поиска"""
        locator = d_locator.get(element)
        if locator:
            return locator.by, locator.locator
        else:
            raise ValueError(f"Локатор для элемента {element} не найден")

    def select_box(self, d_locator:dict, element: str, timeout = 4) -> bool:
        """ Выбрать элемент """
        try:

            by, locator = self.type_find(d_locator, element)

            self.click( by, locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def delete(self, d_locator: dict) -> bool:
        """ Удалить элемент со страницы """
        try:
            element = self.find_element(d_locator.get("by"), d_locator.get("locator") )
            self.driver.execute_script("arguments[0].remove()", element)
            self.click_blunk()
            return True
        except TimeoutException:
            return False

    def send_information (self, d_locator:dict, element: str, what_send: str, timeout = 3) -> bool:
        """ ввести данные в поле"""
        try:
            by, locator = self.type_find(d_locator, element)
            element = self.find_element(by, locator)
            element.send_keys(what_send)
            time.sleep(timeout)
            return True
        except TimeoutException:
            return False