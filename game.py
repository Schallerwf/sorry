import itertools
import random

from board import Board
from sorry_constants import *
from strategy import Strategy

class Game:
    def __init__(self):
        self.board = Board()
        self.currentPlayerIndex = 0
        self.winner = None
        self.strategies = {Y:Strategy('Y'),G:'random',B:'random',R:'random'}
        self.totalTurns = 0
        self.sorryCount = {Y:0,G:0,B:0,R:0}
        self.lostTurns  = {Y:0,G:0,B:0,R:0}
        self.states = []

    def winnerToInt(self):
        return PLAYERS.index(self.winner)

    def setPawns(self, pawns):
        self.board.setPawns(pawns)

    def chooseMove(self, player, possibleStates):
        strategy = self.strategies[player]

        if not possibleStates:
            return None

        if strategy == 'random':
            return random.choice(possibleStates)

        return strategy.chooseMove(possibleStates)

    def playTurn(self):
        card = self.board.drawCard();
        currentPlayer = PLAYERS[self.currentPlayerIndex]
        possibleGameStates = self.computePossibleGameStates(card, currentPlayer)
        move = self.chooseMove(currentPlayer, possibleGameStates)

        if move:
            self.setPawns(move)
            if card == 'sorry':
                self.sorryCount[currentPlayer] += 1
            self.states.append(",".join(self.board.toArray()))
        else:
            self.lostTurns[currentPlayer] += 1

        if self.board.pawns[currentPlayer] == ["home","home","home","home"]:
            self.winner = currentPlayer

        if not move or (move and card != 2):
            self.currentPlayerIndex = (self.currentPlayerIndex + 1) % 4
        self.totalTurns += 1

    def computePossibleGameStates(self, card, player):
        possibleStates = []
        pawnsInPlay = self.board.pawnsInPlay(player)
        numPawnsAtStart = self.board.numPawnsAtStart(player)
        opponentPawnsInPlay = self.board.opponentPawnsInPlay(player)

        if ((card == 1 or card == 2) and numPawnsAtStart > 0):
            possibleStates.append(self.board.startPawn(player))
        
        if (card == 'sorry' and numPawnsAtStart > 1):
            for opponentPawn in opponentPawnsInPlay:
                possibleStates.append(self.board.sorry(player, opponentPawn))
        
        if (pawnsInPlay > 0):
            if (card == 7 and pawnsInPlay > 1):
                possibleCombinations = itertools.combinations(pawnsInPlay, 2)
                for pawnCombination in possibleCombinations:
                    for possibleSplit in POSSIBLE_SEVEN_SPLITS:
                        tmpPawns = self.board.movePawn(player, pawnCombination[0], possibleSplit[0])
                        if tmpPawns:
                            tmpBoard = Board()
                            tmpBoard.setPawns(tmpPawns)
                            tmpPawns = (tmpBoard.movePawn(player, pawnCombination[1], possibleSplit[1]))

                        if tmpPawns:
                            possibleStates.append(tmpPawns)
                        else:
                            tmpPawns = self.board.movePawn(player, pawnCombination[1], possibleSplit[1])
                            if (tmpPawns):
                                tmpBoard = Board()
                                tmpBoard.setPawns(tmpPawns)
                                possibleStates.append(tmpBoard.movePawn(player, pawnCombination[0], possibleSplit[0]))

                        tmpPawns = self.board.movePawn(player, pawnCombination[0], possibleSplit[1])
                        if tmpPawns:
                            tmpBoard = Board()
                            tmpBoard.setPawns(tmpPawns)
                            tmpPawns = (tmpBoard.movePawn(player, pawnCombination[1], possibleSplit[0]))

                        if tmpPawns:
                            possibleStates.append(tmpPawns)
                        else:
                            tmpPawns = self.board.movePawn(player, pawnCombination[1], possibleSplit[0])
                            if (tmpPawns):
                                tmpBoard = Board()
                                tmpBoard.setPawns(tmpPawns)
                                possibleStates.append(tmpBoard.movePawn(player, pawnCombination[0], possibleSplit[1]))
 
            if (card == 11):
                for playablePawn in self.board.pawnsInPlay(player, includeSafe=False):
                    for opponentPawn in opponentPawnsInPlay:
                        possibleStates.append(self.board.swap(player, playablePawn, opponentPawn))

            if (card == 10):
                for playablePawn in pawnsInPlay:
                    possibleStates.append(self.board.movePawn(player, playablePawn, -1))

            if (card == 4):
                for playablePawn in pawnsInPlay:
                    possibleStates.append(self.board.movePawn(player, playablePawn, -4))
            elif (isinstance(card, int)):
                for playablePawn in pawnsInPlay:
                    possibleStates.append(self.board.movePawn(player, playablePawn, card))

        return [x for x in possibleStates if x is not None]