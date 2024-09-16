"""Карты для корова006."""
from typing import Self


class Card:
    
    NUMBERS = list(range(1,105))
    SHTRAF = (1,2,3,5,7)
    def __init__(self, num: int, shtraf: int):
        if num not in Card.NUMBERS:
            raise ValueError
        if shtraf not in Card.SHTRAF:
            raise ValueError
        self.num = num
        self.shtraf = shtraf
    def __repr__(self):
        return f'{self.shtraf}{self.shtraf}'
    def save(self):
        return repr(self)
    

    def load(number: int):
        """From 3 to Card(30, 3)."""
        return Card(num=number[0], shtraf=int(number[1]))

    