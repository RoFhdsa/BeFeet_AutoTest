import time
from dataclasses import dataclass

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from DATA.data_web_find import MainPateLocator as mpl , Weekends as wk
from PEGAS.mediator import Mediator

class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""
    def __init__(self,driver):
        super().__init__(driver)
        self.locators_mpl = mpl().locator_div
        self.locators_wk = wk().locator_div


    def buy_products (self,
                      type_program: str,
                      time_use_program: str,
                      is_weekend: bool,
                      # is_coupon: bool, coupon:str, number_phone, is_friend: bool,
                      ) -> str:

        # 1 check_type_program
        is_check_element = self.check_element(self.locators_mpl, type_program)
        # 2 choice_time_use_program
        self.select_box(self.locators_mpl, time_use_program)

        # 3 choice_is_weekend
        if is_weekend:
            self.select_box(self.locators_wk, is_weekend)
            time.sleep(3)
            self.select_box(self.locators_wk, "Понятно")
            # рассмотреть вариант удаления всплывающего окна
            # d = self.delete()
            # print(f' d = {d}')
            time.sleep(3)
        # 4 choice_is_coupon
        # 5 inpit_number_phone
        # 6 choice_is_friend

        # names_products_choices = [row.get('name') for row in products_choices]
        # self.add_product_to_basket (names_products_choices, pc.locator_xpath_products)
        # # перейти в корзину, сверить продукт, ктоорый был заявлен с тем, который был куплен
        # self.click(by=By.XPATH, locator='//*[@id="shopping_cart_container"]/a')
        # product_page = self.get_products_basket(pb.locator_xpath_products)

        #products = self.get_all_elements(By.CSS_SELECTOR, pc.locator_product)
        #product_choice = [element for element in products if element.text.lower() == product_name['name'].lower()][0]
        #print(f' product_choice = {product_choice, type (product_choice), product_choice.text}')
        # button = product_choice.find_element(By.XPATH,
        #button = self.click(By.CSS_SELECTOR,
         #                                      'button.btn.btn_primary.btn_small.btn_inventory')

        #print(f' button = {button}')
        # выбрать 4 проудкта и добавив их в корзину
        # проверить, что 4 проудкта выбраны и добавлены в корзину (значок корзины)
        # перейти в корзину
        # проверить, что выбраны те продукты, которые были куплены
        # оформить заказ
        # дойти до конечной формы
        # product_page = self.get_products_with_page_catalogs()
        # screenshot = self.create_screenshot(username)
        # allure.attach.file(screenshot, attachment_type=allure.attachment_type.PNG)
        #
        # allure.attach.file(screenshot, attachment_type=allure.attachment_type.PNG)
        # print(f'product_page ={product_page}')
        # return product_page
        pass