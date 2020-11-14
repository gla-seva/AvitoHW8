from dict2class import Dict2Class
from mixin import ColorizeMixin


class AdvertBase:
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, AdvertBase, Dict2Class):
    """
    Парсер json фалйов содержащим иформацию о товаре
    """
    def __init__(self, json_loader):
        super().__init__(json_loader)
        self.price  # проверка на неотрицательность

    @property
    def price(self):
        price = self.content.get('price', 0)
        if price < 0:
            raise ValueError('must be >= 0')
        return price
