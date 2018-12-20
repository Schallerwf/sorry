from sorry_constants import *

class Strategy:
    def __init__(self, player, startWeight=0, homeWeight=65, safeWeight=0, maximize=True):
        self.startWeight = startWeight
        self.homeWeight = homeWeight
        self.safeWeight = safeWeight
        self.player = player
        self.maximize = maximize

    def chooseMove(self, possibleStates):
        ndx = 0
        maxDistance = 0
        minDistance = 200
        chosenMaxNdx = 0
        chosenMinNdx = 0
        for possibleState in possibleStates:
            distances = self.totalDistances(possibleState)
            playerDistance = distances[self.player]
            if playerDistance > maxDistance:
                chosenMaxNdx = ndx
                maxDistance = playerDistance
            if playerDistance < minDistance:
                chosenMinNdx = ndx
                minDistance = playerDistance
            ndx += 1
        if self.maximize:
            return possibleStates[chosenMaxNdx]
        else:
            return possibleStates[chosenMinNdx]
    
    def totalDistance(self, player, playersPawns):
        result = 0
        for pawn in playersPawns:
            if pawn == 'start':
                result += self.startWeight
            elif pawn == 'home':
                result += self.homeWeight
            elif 'safe' in pawn:
                result += self.safeWeight
                result += int(pawn.split(':')[1])
            else:
                result += (int(pawn.split(':')[1]) - PLAYER_OFFSETS[player]) % 60
        return result

    def totalDistances(self, pawns):
        distances = {}
        for player in PLAYERS:
            playersPawns = pawns[player]
            distances[player] = self.totalDistance(player, playersPawns)
        return distances