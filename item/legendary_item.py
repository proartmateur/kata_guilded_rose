from item.item import Item


class LegendaryItem(Item):
    """
    Item común y corriente de la tienda
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __repr__(self):
        return super().__repr__()

    def update(self):
        pass