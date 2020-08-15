from src.item.item import Item


class ConjuredItem(Item):
    """
    Item común y corriente de la tienda
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.__quality_down_speed = 2

    def __repr__(self):
        return super().__repr__()

    def update(self):
        if self.is_expired():
            self.quality -= self.__quality_down_speed * 2
        else:
            self.quality -= self.__quality_down_speed

        self.constraints()

        self.sell_in -= 1

    def is_expired(self):
        if self.sell_in < 0:
            return True
        return False

    def constraints(self) -> None:
        if self.quality < self._quality_min:
            self.quality = self._quality_min
        if self.quality > self._quality_max:
            self.quality = self._quality_max

