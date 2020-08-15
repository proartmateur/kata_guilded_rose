from src.item.item import Item
from src.item.normal_item import NormalItem
from src.item.legendary_item import LegendaryItem
from src.item.bree_item import BreeItem
from src.item.backstage_item import BackStageItem
from src.item.conjured_item import ConjuredItem


def make_item(name: str, sell_in: int, quality: int) -> Item:
    """
    Entrega un Item del tipo según la condición
    :param name:
    :param sell_in:
    :param quality:
    :return: Item
    """

    item_types = [
        {
            "type": BackStageItem,
            "match": "Backstage passes"
        },
        {
            "type": BreeItem,
            "match": "Aged Brie"
        },
        {
            "type": ConjuredItem,
            "match": "Conjured"
        },
        {
            "type": LegendaryItem,
            "match": "Sulfuras"
        },
        {
            "type": NormalItem,
            "match": ""
        }
    ]

    for item_type in item_types:
        if item_type["match"].upper() in name.upper():
            return item_type["type"](name, sell_in, quality)
