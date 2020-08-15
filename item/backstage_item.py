from item.item import Item


class BackStageItem(Item):
    """
    Item común y corriente de la tienda
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __repr__(self):
        return super().__repr__()

    def update(self):

        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += self._quality_down_speed * 3
        elif self.sell_in < 10:
            self.quality += self._quality_down_speed * 2
        else:
            self.quality += self._quality_down_speed

        self.constraints()

        self.sell_in -= 1

    def constraints(self) -> None:
        if self.quality < self._quality_min:
            self.quality = self._quality_min
        if self.quality > self._quality_max:
            self.quality = self._quality_max
