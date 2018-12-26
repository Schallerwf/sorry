from sorry_constants import *
from board import Board

import pickle
import random

RANDOM = 'random'
SIMPLE = 'simple'
RANDOM_FOREST = 'random_forest'

class Strategy:
    def __init__(self, player, strategy=SIMPLE, startWeight=0, homeWeight=66, safeWeight=60, maximize=True, randomForestModel=None):
        self.weights = {'start': startWeight, 'home': homeWeight, 'safe': safeWeight}
        self.player = player
        self.maximize = maximize
        self.strategy = strategy
        self.rfModel = randomForestModel

    def chooseMove(self, possibleStates):
        if (self.strategy == RANDOM):
            return random.choice(possibleStates)

        board = Board()
        ndx = 0
        maxDistance = 0
        minDistance = 200
        chosenMaxNdx = 0
        chosenMinNdx = 0
        for possibleState in possibleStates:
            if (self.strategy == SIMPLE):
                scores = board.totalDistances(possibleState, self.weights)
            elif (self.strategy == RANDOM_FOREST):
                scores = board.rfScores(possibleState, self.rfModel)
            playerDistance = scores[self.player]
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