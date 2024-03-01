import allure
import pytest

from data_case import TestCaseBuyProducts


@allure.feature("Проверка продуктовой страницы")
class TestProductPage:
    @allure.title("Тест проверки приобритения программы")
    @allure.description("Проверка приобритения программы")
    @pytest.mark.parametrize("test_case",
                             [  TestCaseBuyProducts.positive_case,
        TestCaseBuyProducts.positive_case_without_weekend,
        TestCaseBuyProducts.negative_case_break_phone],
                             )
    def test_check_products(self, main_page, main_page_ff, test_case):
        data_case = test_case.get ("data_case")
        expected_result_test = test_case.get ("result_test")

        with allure.step(f"Проверка формы заказача на сайте Chromium"):
            result_test = main_page.buy_products(type_program=data_case.type_program,
                                                 period_use_program=data_case.period_use_program,
                                                 is_weekend=data_case.is_weekend,
                                                 is_coupon=data_case.is_coupon, coupon=data_case.coupon,
                                                 is_number_phone=data_case.is_number_phone,
                                                 number_phone=data_case.number_phone,
                                                 is_friend=data_case.is_friend,
                                                 number_phone_friend=data_case.number_phone_friend,
                                                 expected_page=data_case.expected_page)
            print(f'expected_result_test = {expected_result_test.__dict__}')
            print(f'result_test = {result_test.__dict__}')
            assert  expected_result_test == result_test

        # with allure.step(f"Проверка формы заказача на сайте Mozila"):
        #     result_test = main_page_ff.buy_products(type_program=data_case.type_program,
        #                                          period_use_program=data_case.period_use_program,
        #                                          is_weekend=data_case.is_weekend,
        #                                          is_coupon=data_case.is_coupon, coupon=data_case.coupon,
        #                                          is_number_phone=data_case.is_number_phone,
        #                                          number_phone=data_case.number_phone,
        #                                          is_friend=data_case.is_friend,
        #                                          number_phone_friend=data_case.number_phone_friend,
        #                                          expected_page=data_case.expected_page)
        #     print(f'expected_result_test = {expected_result_test.__dict__}')
        #     print(f'result_test = {result_test.__dict__}')
        #     assert  expected_result_test == result_test

        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.link("https://tracker.yandex.ru/TLB-1", name="Задача:    TLB-1: Проверка формы Заказа")
        allure.link("https://tracker.yandex.ru/TLB-2", name="Баг:   TLB-2: TLB-3: [пром] Форма заказа - отсутствие валидации поля Номер купона")
        allure.link("https://tracker.yandex.ru/TLB-3", name="Баг:   TLB-3: TLB-3: [пром] Форма заказа - отсутствие валидации кода телефона")
