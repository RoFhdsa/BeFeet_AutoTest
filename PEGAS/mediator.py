import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PEGAS.base import Base


class Mediator(Base):

    def check_element (self, d_locator:dict, element: str) -> True or TimeoutException:
        try:
            by, locator = self.type_find(d_locator, element)
            elements = self.get_all_elements(by, locator)
            self.scroll_page(elements[0])
            print(f' elements = {elements}')
            for j in elements:
                print(f' j = {j}')
                print(f' j = {j.text}')
            return True
        except TimeoutException:
            return False

    def type_find(self, d_locator, element) -> By and str or ValueError:
        print(f'  d_locator = { d_locator, type ( d_locator)}')
        locator = d_locator.get(element)
        if locator:
            return locator.by, locator.locator
        else:
            raise ValueError(f"Локатор для элемента {element} не найден")

    def select_box(self, d_locator:dict, element: str, timeout = 2) -> bool:
        try:

            by, locator = self.type_find(d_locator, element)
            print(f' by, locator = {by, locator}')
            self.click( by, locator, timeout=timeout)
            return True
        except TimeoutException:
            print('не нажал')
            return False

    def delete(self, d_locator: dict) -> bool:
        """ Удалить элемент со страницы """
        try:
            #By.XPATH, '//*[@id="header"]/div[7]/div[2]/div[22]/div[2]'
            element = self.find_element(d_locator.get("by"), d_locator.get("locator") )
            self.driver.execute_script("arguments[0].remove()", element)
            self.click_blunk()
            return True
        except TimeoutException:
            print('не удалил')
            return False
        # Delete element:

    def send_information (self, d_locator:dict, element: str, what_send: str, timeout = 3) -> bool:
        try:
            print(f' what_send = {what_send}')
            by, locator = self.type_find(d_locator, element)
            element = self.find_element(by, locator)
            element.send_keys(what_send)
            time.sleep(timeout)
            return True
        except TimeoutException:
            print('объект не найден')
            return False



#     def get_element_by_attribute(self, attribute_name: str, attribute_value: str) -> WebElement:
#         """
#                 вернет элемент по его атрибуту
#         :param attribute_name:
#         :param attribute_value:
#         """
#         element_by_attribute = f"//*[@{attribute_name}='{attribute_value}']"
#         print(f'element_by_attribute = {element_by_attribute}')
#         return self.wait_element_located(locator=element_by_attribute, timeout=10)
#
#     def get_products (self, locator_xpath) -> list:
#
#         elements = self.get_all_elements(By.XPATH, locator_xpath)
#         products = []
#         for element in elements:
#             print(f'element.text = {element.text}')
#             product = Product (
#                 name= element.find_element(By.CLASS_NAME,
#                                                    'inventory_item_name') , # Получаем название товара,
#                 price= element.find_element(By.CLASS_NAME, 'inventory_item_price'),  # Получаем цену товара,
#                 image= element.find_element(By.CLASS_NAME, 'inventory_item_img')
#                             .find_element(By.TAG_NAME,'img').get_attribute('src'),  # Получаем атрибут 'src' картинки
#                 button_buy=element.find_element (By.CSS_SELECTOR, 'button.btn.btn_primary.btn_small.btn_inventory'),
#                 description=element.find_element(By.CLASS_NAME, 'inventory_item_desc'),
#             )
#             products.append(product)
#         return products
#
#     def get_products_with_page_catalogs (self, locator) -> list:
#         element_data = []
#         products = self.get_products(locator)
#         for product in products:
#             product_d = {}
#             product_d['name'] = product.name.text
#             product_d['price'] = product.price.text
#             product_d['image'] = product.image
#             element_data.append(product_d)
#         return element_data
#
#     def add_product_to_basket (self, names_choices_products, locator) -> list:
#         products_page = self.get_products(locator)
#         products_choices = [[product for product in products_page
#             if product.name.text.lower() == name.lower()] for name  in names_choices_products]
#         # product_choice = [product for product in products_page if product.name.text.lower() == name_choice_product.lower()]
#
#         for product_choice in products_choices:
#             print(f' product_choice = {product_choice[0].name.text}')
#         # print(f' name_choice_product = {name_choice_product}')
#             r = product_choice[0].button_buy.click()
#
#     def get_products_basket (self, locator_xpath) -> list:
#
#         elements = self.get_all_elements(By.XPATH, "//div[@class='cart_item']//div[@class='inventory_item_name']")
#         products = []
#         for element in elements:
#             print(4 * '======')
#             print(f'element.text 2 = {element.text}')
#             # product = Product (
#             try:
#                 name_element= element.find_elements(By.CLASS_NAME,'cart_item')
#                 # name = self.find_element(By.CLASS_NAME,'inventory_item_name')
#                 # print(f' namename = {name[0].text}')
#                 print(f' name_elementname_element = {name_element.text}')
#             except:
#                 pass
#             print(4*'======')
#             time.sleep(2)
#         return products
#
#
#
#
# class Product ():
#
#     def __init__(self,name, price, image, button_buy, description):
#         self.name = name
#         self.price = price
#         self.image = image
#         self.button_buy = button_buy
#         self.description = description