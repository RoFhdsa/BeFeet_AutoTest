from dataclasses import dataclass, field

from selenium.webdriver.common.by import By


@dataclass
class Client:
    """список пользователей"""
    name: str = "Albert"
    number_phone: str = 1119029320
    address: str = "ул. Джангара, 19, Элиста, Респ. Калмыкия, 358007"
    number_phone_friend: str = 1019029320
    coupon: str = "BEFITNEW"
    email: str = "test_email@gmail.com"
@dataclass
class ClientError:
    """список полей на странице аутентификации"""
    name: str = 1000*"Albert"
    number_phone: str = 1119029320
    address: str = 1000*"ул. Джангара, 19, Элиста, Респ. Калмыкия, 358007"
    number_phone_friend: str = 1019029320
    coupon: str = 1000*"MQ029DF"
    email: str = 1000*"test_email@gmail.com"
