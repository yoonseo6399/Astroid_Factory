from enum import Enum


class ItemType(Enum):
    STEEL = "steel"



class Item:
    type = ItemType.STEEL

    def __init__(self,itemtype):
        type = itemtype







print(ItemType.STEEL)