import allure
import pytest

from DATA.data_test import Client


@allure.feature("Проверка продуктовой страницы")
class TestProductPage:
    @allure.title("Тест проверки приобритения программы")
    @allure.description("Проверка приобритения программы")
    @pytest.mark.parametrize(
        "type_program, period_use_program, is_weekend,"
        "is_coupon, coupon, number_phone,"
        "is_friend, number_phone_friend",
        [
            ("Заказать Extralight", "4 недели", True,
             True, Client.coupon, Client.number_phone,
             True, Client.number_phone_friend),
        ]
    )
    def test_check_products(self, main_page, type_program, period_use_program, is_weekend,
                            is_coupon, coupon, number_phone,
                            is_friend, number_phone_friend):

        main_page.buy_products(type_program=type_program,
                               period_use_program=period_use_program, is_weekend=is_weekend,
                               is_coupon=is_coupon, coupon=coupon, number_phone=number_phone,
                               is_friend =is_friend, number_phone_friend= number_phone_friend)
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
