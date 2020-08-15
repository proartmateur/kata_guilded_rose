from src.item.item import Item, ItemProps


class BreeItem(Item, ItemProps):
    """
    Item común y corriente de la tienda
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __repr__(self):
        return super().__repr__()

    def update(self):
        self.quality += self._quality_down_speed
        self.constraints()

        self.sell_in -= 1

    def constraints(self) -> None:
        if self.quality < self._quality_min:
            self.quality = self._quality_min
        if self.quality > self._quality_max:
            self.quality = self._quality_max
