import csv
import os.path
from src.InstantiateCSVError import InstantiateCSVError


class Item(InstantiateCSVError):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Отсутствует файл {path}")
        cls.all.clear()
        with open(path, newline="", encoding="cp1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row.get("name") or not row.get("price") or not row.get("quantity"):
                    raise InstantiateCSVError(path)
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)
    @staticmethod
    def string_to_number(string):
        """Статический метод, возвращающий число из числа-строки"""
        numbers = []
        for number in string:
            if number.isdigit():
                numbers.append(number)
            else:
                None
        return (int(numbers[0]))
