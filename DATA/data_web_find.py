from dataclasses import dataclass, field

from selenium.webdriver.common.by import By



@dataclass
class ElementLocator:
    name: str
    by: By
    locator: str

@dataclass
class MainPateLocator:
    locator_div: dict = field(default_factory=lambda:
    {'Заказать Extralight': ElementLocator(name="Extralight",
                                  by=By.XPATH,
                                  locator='//*[@id="order"]/div/div/div[1]/div[1]/div[1]'),

     'Неделя': ElementLocator(name="Неделя (7 дней)",
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
    locator_div: dict = field(default_factory=lambda:
    {True: ElementLocator(name="Исключить выходные",
                                           by=By.XPATH,
                                           locator='//*[@id="order"]/div/div/div[2]/div[2]/div/label/div/div[2]'),
     "Понятно": ElementLocator(name="Понятно",
                          by=By.XPATH,
                          locator='//*[@id="header"]/div[7]/div[2]/div[22]/div[2]/div[3]')})
