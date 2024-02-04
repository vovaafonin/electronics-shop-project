"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from config import PATH_TO_CSV
from src.item import Item
from src.phone import Phone
from src.InstantiateCSVError import InstantiateCSVError
import os.path

item1 = Item("Iphone 12", 60000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 300000


def test_apply_discount():
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 30000


def test_string_to_number():
    assert Item.string_to_number('4') == 4
    assert Item.string_to_number('fasdf85.2') == 8


def test_instantiate_from_csv():
    Item.instantiate_from_csv(PATH_TO_CSV)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == "Смартфон"


def test_setter_name():
    item1.name = "смартфон"
    assert item1.name == "смартфон"
    item1.name = "суперсмартфон"
    assert item1.name == "суперсмарт"


def test_repr():
    item1 = Item("смартфон", 50000, 4)
    assert repr(item1) == "Item('смартфон', 50000, 4)"


def test_str():
    item1 = Item("смартфон", 50000, 4)
    assert str(item1) == 'смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1 + item1 == 10
    phone1 = Phone("iPhone 14", 120000, 10, 2)
    assert phone1 + item1 == 15


def test_csv_file_exceptions():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("file.txt")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items2.csv")
