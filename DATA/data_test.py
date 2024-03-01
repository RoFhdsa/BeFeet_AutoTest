from dataclasses import dataclass, field

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
    number_phone: str = 'Dl-10.'
    address: str = 1000*"ул. Джангара, 19, Элиста, Респ. Калмыкия, 358007"
    number_phone_friend: str = '1rP[s-7'
    coupon: str = 10*"MQ029DF"
    email: str = 1000*"test_email@gmail.com"
@dataclass
class Program:
    """данные о приобритаемой программе"""
    name: str = "Extralight"
    period_use_program: dict = field(default_factory=lambda:
    {'1w':  'Неделя',
     '2w': '2 недели',
     '4w': '4 недели',
     '2M': '2 месяца',
     '3M': '3 месяца',
     })
@dataclass
class FinishWebPage:
    """данные о странице которую ожидаем в результате теста"""
    expected_page_true: str = "https://letbefit.ru/order/"
    expected_page_false: str = "https://letbefit.ru/"
