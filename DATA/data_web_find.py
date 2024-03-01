from dataclasses import dataclass, field

from selenium.webdriver.common.by import By


@dataclass
class ElementLocator:
    name: str
    by: By
    locator: str


@dataclass
class ProgramName:
    locator_div: dict = field(default_factory=lambda:
    {'Extralight': ElementLocator(name="Extralight",
                                           by=By.XPATH,
                                           locator='//*[@id="order"]/div/div/div[1]/div[1]/div[1]')})


@dataclass
class Spam:
    locator_div: dict = field(default_factory=lambda:
    {True: ElementLocator(name="удалить спам",
                          by=By.XPATH,
                          locator='/html/body[1]/div[1]')})


@dataclass
class PeriodUseProgrammL:
    locator_div: dict = field(default_factory=lambda:
    {'Неделя': ElementLocator(name="Неделя (7 дней)",
                              by=By.XPATH,
                              locator=f"//div[contains(text(), 'Неделя (7 дней)')]/ancestor::div[contains(@class, 'contract-config__el')]/div/label"),
     '2 недели': ElementLocator(name="2 недели (14 дней)",
                                by=By.XPATH,
                                locator=f"//div[contains(text(), '2 недели (14 дней)')]/ancestor::div[contains(@class, 'contract-config__el')]/div/label"),
     '4 недели': ElementLocator(name="4 недели (28 дней)",
                                by=By.XPATH,
                                locator=f"//div[contains(text(), '4 недели (28 дней)')]/ancestor::div[contains(@class, 'contract-config__el')]/div/label"),
     '2 месяца': ElementLocator(name="2 месяца (56 дней)",
                                by=By.XPATH,
                                locator=f"//div[contains(text(), '2 месяца (56 дней)')]/ancestor::div[contains(@class, 'contract-config__el')]/div/label"),
     '3 месяца': ElementLocator(name="3 месяца (84 дня)",
                                by=By.XPATH,
                                locator=f"//div[contains(text(), '3 месяца (84 дня))]/ancestor::div[contains(@class, 'contract-config__el')]/div/label"),
     })


@dataclass
class Weekends:
    delete_block: dict = field(default_factory=lambda:
    {'locator': '//*[@id="header"]/div[7]/div[2]/div[22]',
     'by': By.XPATH})

    check_msg: dict = field(default_factory=lambda:
    {True: ElementLocator(name="Исключить выходные",
                          by=By.XPATH,
                          locator='//*[@id="header"]/div[7]/div[2]/div[22]/div[2]/div[2]/p')})

    locator_div: dict = field(default_factory=lambda:
    {True: ElementLocator(name="Исключить выходные",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[2]/div/label/div/div[2]'),
     "It's clear": ElementLocator(name="нажать понятно",
                               by=By.XPATH,
                               locator='//*[@id="header"]/div[7]/div[2]/div[22]/div[2]/div[3]'),
     "clear_block": ElementLocator(name="закрыть окно выходные",
                                                         by=By.XPATH,
                                                         locator='//*[@id="header"]/div[7]/div[2]/div[22]')
     })


@dataclass
class Coupon:
    locator_div: dict = field(default_factory=lambda:
    {"input_coupon": ElementLocator(name="поле ввода купона",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[5]/div/div[1]/input'),
     True: ElementLocator(name="купон кнопка",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[4]/div/label/div/div[2]'),
    "button_apply": ElementLocator(name="кнопка применить",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[5]/div/div[3]/div'),
    "ErrorCoupon": ElementLocator(name="кнопка не подходит",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[5]/div/div[1]/div'),
     })

@dataclass
class Phone:
    locator_div: dict = field(default_factory=lambda:
    {True: ElementLocator(name="телефон",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[6]/div/input'),
     "ErrorPhone": ElementLocator(name="не корректный телефон",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[6]/div/div'),
     "ErrorPhone_with_coupon": ElementLocator(name="не корректный телефон",
                                  by=By.XPATH,
                                  locator='//*[@id="order"]/div/div/div[2]/div[5]/div/div[2]/div')
     })
@dataclass
class AdviceFriend:
    locator_div: dict = field(default_factory=lambda:
    {True: ElementLocator(name="есть телефон друга",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[7]/div/div/label/div/div[2]'),
     "input_phone": ElementLocator(name="поле ввода номера телефона",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[8]/div/div/input'),
     "ErrorPhoneFriend": ElementLocator(name="поле ввода номера телефона",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[2]/div[8]/div/div/div')
     })

@dataclass
class Checout:
    locator_div: dict = field(default_factory=lambda:
    {"button_checkout": ElementLocator(name="оформить заказ",
                          by=By.XPATH,
                          locator='//*[@id="order"]/div/div/div[3]/div[2]'),
     })