from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.ICE_PATH_B2F_BLACKTHORN_SIDE

class ICE_PATH_B2F_BLACKTHORN_SIDE(IntEnum):
	def __str__(self):
		return str(self.value)

	ICE_PATH_B1F_8 = 1
	ICE_PATH_B3F_2 = 2


class Ice_Path_B2F_Blackthorn_Side_Warp_Points(Enum): 

	ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B1F_8_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_BLACKTHORN_SIDE.ICE_PATH_B1F_8), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	ICE_PATH_B2F_BLACKTHORN_SIDE_TO_ICE_PATH_B3F_2_WP = WarpInstruction( 
		getHex(ICE_PATH_B2F_BLACKTHORN_SIDE.ICE_PATH_B3F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

