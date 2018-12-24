from sorry_constants import *
from board import Board

class Strategy:
    def __init__(self, player, startWeight=0, homeWeight=65, safeWeight=60, maximize=True):
        self.weights = {'start': startWeight, 'home': homeWeight, 'safe': safeWeight}
        self.player = player
        self.maximize = maximize

    def chooseMove(self, possibleStates):
        board = Board()
        ndx = 0
        maxDistance = 0
        minDistance = 200
        chosenMaxNdx = 0
        chosenMinNdx = 0
        for possibleState in possibleStates:
            distances = board.totalDistances(possibleState, self.weights)
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