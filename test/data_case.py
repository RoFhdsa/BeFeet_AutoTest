from dataclasses import dataclass

from DATA.data_test import Client, Program, ClientError, FinishWebPage


@dataclass
class TestCase:
    type_program: str
    period_use_program: str
    is_weekend: bool
    is_coupon: bool
    coupon: str
    is_number_phone: bool
    number_phone: bool
    is_friend: bool
    number_phone_friend: str
    expected_page: str


class ResultCheck:

    def __init__(self, check_type_program: bool, choice_time_use_program: bool, choice_is_weekend: bool,
                 input_number_phone: bool, choice_is_coupon: bool, choice_is_friend: bool, checkout_order: bool,
                 is_expected_page: bool, input_number_phone_friend: bool):
        self.check_type_program = check_type_program
        self.choice_time_use_program = choice_time_use_program
        self.choice_is_weekend = choice_is_weekend
        self.input_number_phone = input_number_phone
        self.choice_is_coupon = choice_is_coupon
        self.choice_is_friend = choice_is_friend
        self.checkout_order = checkout_order
        self.is_expected_page = is_expected_page
        self.input_number_phone_friend = input_number_phone_friend

    def __eq__(self, other):
        return all(getattr(self, attr) == getattr(other, attr) for attr in self.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __del__(self):
        pass


class TestCaseBuyProducts:
    positive_case = {
        "data_case": TestCase(Program().name, Program().period_use_program.get('1w'), True,
                              True, Client().coupon,
                              True, Client().number_phone,
                              True, Client().number_phone_friend,
                              FinishWebPage.expected_page_true),
        "result_test": ResultCheck(check_type_program=True,
                                   choice_time_use_program=True,
                                   choice_is_weekend=True,
                                   input_number_phone=True,
                                   choice_is_coupon=True,
                                   choice_is_friend=True,
                                   checkout_order=True,
                                   is_expected_page=True,
                                   input_number_phone_friend=True)
    }

    positive_case_without_weekend = {
        "data_case": TestCase(Program().name, Program().period_use_program.get('4w'), False,
                              True, ClientError().coupon,
                              True, Client().number_phone,
                              False, '',
                              FinishWebPage.expected_page_true),
        "result_test": ResultCheck(check_type_program=True,
                                   choice_time_use_program=True,
                                   choice_is_weekend=False,
                                   input_number_phone=True,
                                   choice_is_coupon=False,
                                   choice_is_friend=False,
                                   checkout_order=True,
                                   is_expected_page=True,
                                   input_number_phone_friend=False)
    }

    negative_case_break_phone = {
        "data_case": TestCase(Program().name, Program().period_use_program.get('2M'), True,
                              True, ClientError().coupon,
                              True, ClientError().number_phone,
                              True, ClientError().number_phone_friend,
                              FinishWebPage.expected_page_true),
        "result_test": ResultCheck(check_type_program=True,
                                   choice_time_use_program=True,
                                   choice_is_weekend=True,
                                   input_number_phone=False,
                                   choice_is_coupon=True    ,
                                   choice_is_friend=True,
                                   checkout_order=True,
                                   is_expected_page=False,
                                   input_number_phone_friend=False)
    }
