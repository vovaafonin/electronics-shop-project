"""Здесь надо написать тесты с использованием pytest для модуля item."""
from config import PATH_TO_CSV
from src.item import Item

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
