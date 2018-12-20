Y = "Y"
G = "G"
R = "R"
B = "B"
PLAYERS = [Y,G,R,B]
OPPONENTS = {Y:[G,R,B], G:[Y,R,B], R:[Y,G,B], B:[Y,G,R]}
CARDS = [1,2,3,4,5,7,8,10,11,12,'sorry']
POSSIBLE_SEVEN_SPLITS = [[1,6],[2,5],[3,4]]

PLAYER_OFFSETS = {Y:0,G:15,R:30,B:45}
SAFE_ZONE_ENTRANCE = 2
START = 4
SMALL_SLIDE_STARTS = {1:Y,16:G,31:R,46:B}
LARGE_SLIDE_STARTS = {9:Y,24:G,39:R,54:B}