
import time
import random

import pytest
import allure
# from src.Products.ProductSQL import ProductSQL
# from src.Products.product_data import Products

@allure.feature("Проверка продуктовой страницы")
class TestProductPage:
    @allure.title("Тест проверки приобритения программы")
    @allure.description("Проверка приобритения программы")
    @pytest.mark.parametrize(
        "type_program, time_use_program, is_weekend",
        [
            ("Заказать Extralight", "4 недели", True),
             # , "secret_sauce", False),

        ]
    )
    def test_check_products(self, main_page, type_program, time_use_program, is_weekend):
        main_page.buy_products(type_program=type_program,
                               time_use_program=time_use_program,
                               is_weekend=is_weekend)
        pass

        #
        # with allure.step(f"Проверка отображения продуктовой страницы для пользователя {username}"):
        #     product_page = main_page.check_products(username, password)
        #
        #     original_product = ProductSQL.get_product()
        #     for row in product_page:
        #         assert (row in original_product) == result
        # if result:
        #     allure.dynamic.title(f"Успешная проверка продуктовой страницы для {username}")
        #     allure.dynamic.description(f"Продуктовая страница отображается корректно для пользователя {username}")
        # else:
        #     allure.dynamic.title(f"Неудачная проверка продуктовой страницы для {username}")
        #     allure.dynamic.description(f"Продуктовая страница не отображается корректно для пользователя {username}")
        #
        # # allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)
        # allure.dynamic.severity(allure.severity_level.CRITICAL)
        # allure.link("https://jira.example.com/ISSUE-123", name="Related issue")
