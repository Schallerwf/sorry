Y = "Y"
G = "G"
B = "B"
R = "R"
PLAYERS = [Y,G,B,R]
OPPONENTS = {Y:[G,B,R], G:[Y,B,R], B:[Y,G,R], R:[Y,G,B]}
CARDS = [1,2,3,4,5,7,8,10,11,12,'sorry']
POSSIBLE_SEVEN_SPLITS = [[1,6],[2,5],[3,4]]

PLAYER_OFFSETS = {Y:0,G:15,B:30,R:45}
SAFE_ZONE_ENTRANCE = 2
START = 4
SMALL_SLIDE_STARTS = {1:Y,16:G,31:B,46:R}
LARGE_SLIDE_STARTS = {9:Y,24:G,39:B,54:R}