from abc import ABCMeta, abstractmethod


class ItemProps(metaclass=ABCMeta):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self._quality_min = 0
        self._quality_max = 50
        self._quality_down_speed = 1

    def __repr__(self):
        return "%s - %s, %s, %s" % (type(self).__name__, self.name, self.sell_in, self.quality)


class Item(metaclass=ABCMeta):
    """
    Clase abstracta que describe el contrato
    y comportamiento base de un Item.
    """

    @abstractmethod
    def update(self):
        pass
