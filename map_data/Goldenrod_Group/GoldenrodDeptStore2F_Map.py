from enum import IntEnum, Enum
from class_definitions import WarpInstruction, getHex
from map_data.map_constants import MapGroup, Goldenrod
mapGroup = MapGroup.GOLDENROD
specificMap = Goldenrod.GOLDENROD_DEPT_STORE_2F

class GOLDENROD_DEPT_STORE_2F(IntEnum):
	def __str__(self):
		return str(self.value)

	GOLDENROD_DEPT_STORE_3F_1 = 1
	GOLDENROD_DEPT_STORE_1F_3 = 2
	GOLDENROD_DEPT_STORE_ELEVATOR_1 = 3


class Goldenrod_Dept_Store_2F_Warp_Points(Enum): 

	GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_3F_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_2F.GOLDENROD_DEPT_STORE_3F_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_1F_3_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_2F.GOLDENROD_DEPT_STORE_1F_3), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

	GOLDENROD_DEPT_STORE_2F_TO_GOLDENROD_DEPT_STORE_ELEVATOR_1_WP = WarpInstruction( 
		getHex(GOLDENROD_DEPT_STORE_2F.GOLDENROD_DEPT_STORE_ELEVATOR_1), 
		getHex(mapGroup),
		getHex(specificMap)
		) 

