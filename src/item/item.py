from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    """
    Clase abstracta que describe el contrato
    y comportamiento base de un Item.
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self._quality_min = 0
        self._quality_max = 50
        self._quality_down_speed = 1

    def __repr__(self):
        return "%s - %s, %s, %s" % (type(self).__name__, self.name, self.sell_in, self.quality)

    @abstractmethod
    def update(self):
        pass


# class Item:
#     def __init__(self, name, sell_in, quality):
#         self.name = name
#         self.sell_in = sell_in
#         self.quality = quality
#
#     def __repr__(self):
#         return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
