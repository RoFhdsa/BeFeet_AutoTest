import time

import allure

from DATA.data_web_find import (ProgramName as pn, Weekends as wk, PeriodUseProgrammL as pup,
                                Spam as s, Coupon as c, Phone as ph, AdviceFriend as af, Checout as ch)
from PEGAS.mediator import Mediator
from test.data_case import ResultCheck


class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""

    def __init__(self, driver):
        super().__init__(driver)
        self.locator_s = s().locator_div
        self.locators_mpl = pn().locator_div
        self.locators_pup = pup().locator_div
        self.delete_block = wk().delete_block
        self.check_msg = wk().check_msg
        self.locators_wk = wk().locator_div
        self.locator_cl = c().locator_div
        self.locator_ph = ph().locator_div
        self.locator_af = af().locator_div
        self.locator_ch = ch().locator_div

    def buy_products(self,
                     type_program: str, period_use_program: str, is_weekend: bool,
                     is_coupon: bool, coupon: str,
                     is_number_phone: bool, number_phone: str,
                     is_friend: bool, number_phone_friend: str,
                     expected_page: str) -> list:

        # 0 wait spam information
        self.click_blunk()
        self.click_blunk()
        time.sleep(2)

        # 1 check_type_program
        with allure.step(f"Проверка выбранной программы {type_program}"):
            check_type_program = self.check_element(self.locators_mpl, type_program)
            screenshot_product_page = self.create_screenshot(type_program)
            allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)

        # 2 choice_time_use_program
        with allure.step(f"Проверка выбранного времени использования прогрммы {period_use_program}"):
            choice_time_use_program = self.select_box(self.locators_pup, period_use_program)
            screenshot_product_page = self.create_screenshot(period_use_program)
            allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)

        # 3 choice_is_weekend
        if is_weekend:
            with allure.step(f"Проверка выбра Исключить выходные прогрммы {type_program}"):
                self.select_box(self.locators_wk, is_weekend)
                self.check_element(self.check_msg, True)
                screenshot_product_page = self.create_screenshot("выходные_исключить")
                allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)
            choice_is_weekend = self.select_box(self.locators_wk, "It's clear")
        else:
            choice_is_weekend = False

        # 4 input_number_phone
        if is_number_phone:
            with allure.step(f"Проверка ввода номера телефона {number_phone}"):
                self.send_information(self.locator_ph, element=True, what_send=number_phone)
                screenshot_product_page = self.create_screenshot({number_phone})
                allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)

        # 5 choice_is_coupon
        if is_coupon:
            ErrorPhone = "ErrorPhone_with_coupon"

            with allure.step(f"Проверка ввода купона {coupon}"):
                self.select_box(self.locator_cl, element=is_coupon)
                self.send_information(self.locator_cl, element="input_coupon", what_send=coupon)
                self.select_box(self.locator_cl, element="button_apply")

                if self.check_element(self.locator_cl, element="ErrorCoupon"):
                    choice_is_coupon = False
                else:
                    choice_is_coupon = True
                screenshot_product_page = self.create_screenshot({coupon})
                allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)
        else:
            choice_is_coupon = False
            ErrorPhone = "ErrorPhone"

        # 6 choice_is_friend
        if is_friend:
            with allure.step(f"Проверка Befit мне рекомендовал друг"):
                self.select_box(self.locator_af, element=is_friend)
                choice_is_friend = self.send_information(self.locator_af, element="input_phone",
                                                         what_send=number_phone_friend)

                screenshot_product_page = self.create_screenshot({"друг_рекомендовал"})
                allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)
        else:
            choice_is_friend = False
            input_number_phone_friend = False
        # 7 checkout_order
        with allure.step(f"оформить заказ прогрммы {type_program}"):
            checkout_order = self.select_box(self.locator_ch, element="button_checkout", timeout=20)
            time.sleep(10)

            # 7-1 check break phone
            if self.check_element(self.locator_ph, element=ErrorPhone):
                input_number_phone = False
            else:
                input_number_phone = True

            # 7-2 check break phone friend
            if choice_is_friend == True:
                if self.check_element(self.locator_af, element="ErrorPhoneFriend"):
                    input_number_phone_friend = False
                else:
                    input_number_phone_friend = True

            current_page = self.return_actual_url()
            if current_page == expected_page:
                is_expected_page = True
            else:
                is_expected_page = False
            screenshot_product_page = self.create_screenshot({"оформить_программу"})
            allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)
        return ResultCheck(check_type_program, choice_time_use_program, choice_is_weekend, input_number_phone,
                           choice_is_coupon, choice_is_friend, checkout_order, is_expected_page,
                           input_number_phone_friend)
