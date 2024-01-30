import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_repr():
    assert repr(kb) == "Keyboard('Dark Proje', 9600, 5, EN)"


def test_str():
    assert str(kb) == "Dark Proje"


@pytest.fixture
def fix_class():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_change_lang(fix_class):
    fix_class.change_lang()
    assert fix_class.language == "RU"
    fix_class.change_lang()
    assert fix_class.language == "EN"
