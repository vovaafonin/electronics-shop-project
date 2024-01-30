from src.item import Item


class Mixin:

    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"


class Keyboard(Item, Mixin):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self._language})"

    def __str__(self):
        return f"{self.name}"

    @property
    def language(self):
        return self._language
