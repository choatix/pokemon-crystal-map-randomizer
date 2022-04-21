from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Dungeons
mapGroup = MapGroup.DUNGEONS
specificMap = Dungeons.TIN_TOWER_9F

class TIN_TOWER_9F(IntEnum):
	def __str__(self):
		return str(self.value)

	TIN_TOWER_8F_2 = 1
	TIN_TOWER_8F_3 = 2
	TIN_TOWER_8F_4 = 3
	TIN_TOWER_ROOF_1 = 4
	TIN_TOWER_7F_5 = 5
	TIN_TOWER_8F_5 = 6
	TIN_TOWER_8F_6 = 7


class Tin_Tower_9F_Warp_Points(Enum): 

	TIN_TOWER_9F_TO_TIN_TOWER_8F_2_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_8F_2), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_8F_3_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_8F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_8F_4_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_8F_4), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_ROOF_1_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_ROOF_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_7F_5_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_7F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_8F_5_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_8F_5), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	TIN_TOWER_9F_TO_TIN_TOWER_8F_6_WP = WarpInstruction( 
		getHex(TIN_TOWER_9F.TIN_TOWER_8F_6), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

