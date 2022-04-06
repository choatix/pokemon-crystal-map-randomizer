from enum import IntEnum, Enum

from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, New_Bark

mapGroup = MapGroup.NEW_BARK
specificMap = New_Bark.PLAYERS_NEIGHBORS_HOUSE

class NEIGHBORS_HOUSE(IntEnum):
    def __str__(self):
        return str(self.value)

    NEW_BARK_TOWN = 1  # dual wide

class Players_Neighbors_House_Warp_Points(Enum):

    PLAYERS_NEIGHBORS_HOUSE_TO_NEW_BARK_WP = WarpInstruction(
        getHex(NEIGHBORS_HOUSE.NEW_BARK_TOWN),
        getHex(mapGroup),
        getHex(specificMap),
        )


