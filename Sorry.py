import random
import copy
import itertools
import sys
import argparse
import time
from collections import Counter

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

class Board:
    def __init__(self):
        self.deck = self.initDeck()
        self.discardPile = []
        self.pawns = {Y: ["start", "start", "start", "start"],
                      G: ["start", "start", "start", "start"],
                      R: ["start", "start", "start", "start"],
                      B: ["start", "start", "start", "start"],}

    def initDeck(self):
        deck = [1]
        for card in CARDS:
            for x in range(4):
                deck.append(card)
        random.shuffle(deck)
        return deck

    def toArray(self):
        result = []
        for player in PLAYERS:
            playersPawns = self.pawns[player]
            for pawn in playersPawns:
                result.append(str(self.pawnToInt(pawn)))
        return result

    def pawnToInt(self, pawn):
        if 'board' in pawn:
            return int(pawn.split(':')[1]) + 1
        if 'safe' in pawn:
            return int(pawn.split(':')[1]) + 60
        if 'start' == pawn:
            return 0
        if 'home' == pawn: 
            return 66

    def drawCard(self):
        card = self.deck.pop()
        self.discardPile.append(card)

        if len(self.deck) == 0:
            self.deck = self.discardPile
            random.shuffle(self.deck)
            self.discardPile = []

        return card

    def setPawns(self, pawns):
        self.pawns = pawns

    def getStartSpot(self, player):
        return 'board:' + str(START + PLAYER_OFFSETS[player])

    def getSafeSpot(self, player):
        return SAFE_ZONE_ENTRANCE + PLAYER_OFFSETS[player]

    def isSpotSlide(self, player, spotNumber):
        if spotNumber in SMALL_SLIDE_STARTS and SMALL_SLIDE_STARTS[spotNumber] != player:
            return 3
        if spotNumber in LARGE_SLIDE_STARTS and LARGE_SLIDE_STARTS[spotNumber] != player:
            return 4
        return 0

    def startPawn(self, player):
        pawns = copy.deepcopy(self.pawns)
        startSpot = self.getStartSpot(player)
        playerAtSpot = self.pawnAtLocation(pawns, startSpot)

        # invalid move if players own pawn is in the way
        if playerAtSpot == player:
            return None

        # set pawn location to start
        playerPawns = pawns[player]
        playerPawns[playerPawns.index('start')] = startSpot

        # check if opponent pawn should be bumped to start
        if playerAtSpot:
            opponentPawns = pawns[playerAtSpot]
            opponentPawns[opponentPawns.index(startSpot)] = 'start'

        return pawns

    def applySlide(self, player, currentSpot, pawns, originalSpot=None):
        spotParts = currentSpot.split(':')
        newSpot = spotParts[0]
        newSpotNumber = int(spotParts[1])

        slide = self.isSpotSlide(player, newSpotNumber)
        if (slide):
            while slide != 0:
                newSpotNumber += 1
                playerAtSpot = self.pawnAtLocation(pawns, newSpot+':'+str(newSpotNumber))
                if playerAtSpot and originalSpot != newSpot+':'+str(newSpotNumber):
                    playersPawns = pawns[playerAtSpot]
                    playersPawns[playersPawns.index(newSpot+':'+str(newSpotNumber))] = 'start'
                slide = slide - 1
            playerAtSpot = self.pawnAtLocation(pawns, newSpot+':'+str(newSpotNumber))
        return newSpotNumber

    def movePawn(self, player, pawn, distance):
        pawns = copy.deepcopy(self.pawns)

        playerPawns = pawns[player]
        spotParts = pawn.split(':')
        currentSpot = spotParts[0]
        currentSpotNumber = int(spotParts[1])
        newSpot = currentSpot
        newSpotNumberBeforeModulo = (currentSpotNumber + distance)
        newSpotNumber = (currentSpotNumber + distance) % 60
        safeSpot = self.getSafeSpot(player)
        spotsToSafe = safeSpot - newSpotNumber

        # Moving into safe zone?
        if ('board' in newSpot and spotsToSafe < 0 and distance > 0 and not (currentSpotNumber > safeSpot and newSpotNumberBeforeModulo < 60)):
            newSpot = 'safe'
            newSpotNumber = (spotsToSafe * -1)

            if (newSpot+':'+str(newSpotNumber)) in playerPawns:
                return None

        # Moving backward out of safe zone?
        if ('safe' in newSpot and (newSpotNumber < 1 or newSpotNumber > 5) and distance < 0):
            newSpotNumber = (self.getSafeSpot(player) + (distance + currentSpotNumber)) % 60
            newSpot = 'board'

        # Moving into home?
        if ('safe' in newSpot and newSpotNumber > 5):
            playerPawns[playerPawns.index(pawn)] = 'home'
            return pawns

        if ('board' in newSpot):
            playerAtSpot = self.pawnAtLocation(pawns, newSpot+':'+str(newSpotNumber))
            if playerAtSpot == player:
                return None
            if playerAtSpot:
                opponentPawns = pawns[playerAtSpot]
                opponentPawns[opponentPawns.index(newSpot+':'+str(newSpotNumber))] = 'start'

            newSpotNumber = self.applySlide(player, newSpot+':'+str(newSpotNumber), pawns, originalSpot=pawn)
            if newSpotNumber == None:
                return None

        if (newSpot+':'+str(newSpotNumber)) in playerPawns:
            return None

        if pawn in playerPawns:
            playerPawns[playerPawns.index(pawn)] = newSpot+':'+str(newSpotNumber)
        return pawns

    def swap(self, player, playerPawn, opponentPawn):
        pawns = copy.deepcopy(self.pawns)
        playersPawns = pawns[player]
        opponent = self.pawnAtLocation(pawns, opponentPawn)
        opponentPawns = pawns[opponent]

        playersPawns[playersPawns.index(playerPawn)] = opponentPawn
        opponentPawns[opponentPawns.index(opponentPawn)] = playerPawn

        playersPawns[playersPawns.index(opponentPawn)] = 'board:'+str(self.applySlide(player, opponentPawn, pawns))

        # It is possible the opponent pawn was bumped by the player pawn sliding
        if playerPawn in opponentPawns:
            opponentPawns[opponentPawns.index(playerPawn)] = 'board:'+str(self.applySlide(opponent, playerPawn, pawns))

        return pawns

    def sorry(self, player, opponentPawn):
        pawns = copy.deepcopy(self.pawns)
        playersPawns = pawns[player]
        opponent = self.pawnAtLocation(pawns, opponentPawn)
        opponentPawns = pawns[opponent]

        playersPawns[playersPawns.index('start')] =  "board:"+str(self.applySlide(player, opponentPawn, pawns))
        # Might have already gotton bumped from applying the slide
        if opponentPawn in opponentPawns:
            opponentPawns[opponentPawns.index(opponentPawn)] = 'start'
        return pawns

    def numPawnsAtStart(self, player):
         return len([pawn for pawn in self.pawns[player] if 'start' == pawn])

    def pawnsInPlay(self, player, includeSafe=True):
        return [pawn for pawn in self.pawns[player] if 'board' in pawn or (includeSafe and 'safe' in pawn)]

    def opponentPawnsInPlay(self, player):
        result = []
        for opponent in OPPONENTS[player]:
            result += self.pawnsInPlay(opponent, includeSafe=False)
        return result

    def pawnAtLocation(self, pawns, targetLocation):
        for player, locations in pawns.iteritems():
            for location in locations:
                if targetLocation == location:
                    return player
        return None

    def totalDistance(self, player, playersPawns, weights={}):
        result = 0
        for pawn in playersPawns:
            if pawn == 'start':
                result += weights.get('start', 0)
            elif pawn == 'home':
                result += weights.get('home', 65)
            elif 'safe' in pawn:
                result += weights.get('safe', 0)
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

class Game:
    def __init__(self):
        self.board = Board()
        self.currentPlayerIndex = 0
        self.winner = None
        self.strategies = {Y:Strategy('Y'),G:'random',R:'random',B:'random'}
        self.totalTurns = 0
        self.sorryCount = {Y:0,G:0,R:0,B:0}
        self.lostTurns  = {Y:0,G:0,R:0,B:0}
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

def capitalize_keys(d, toLower=False):
    result = {}
    for key, value in d.items():
        upper_key = key.lower() if toLower else key.upper()
        result[upper_key] = value
    return result

def analyzeBoard(pawns, player, card):
    pawns = capitalize_keys(pawns)
    card = int(card) if card.isdigit() else card
    game = Game()
    game.setPawns(pawns)
    possibleGameStates = game.computePossibleGameStates(card, player)

    gameStates = []
    for possibleGameState in possibleGameStates:
        gameStates.append({'gameState': possibleGameState,
                            'distances': game.board.totalDistances(possibleGameState)})

    results = {'inputState': {'distances': game.board.totalDistances(pawns)},
              'gameStates': gameStates}

    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', '-c', default=1, type=int, help='number of sorry games to simulate. defaults to 1')
    parser.add_argument('--outputData', '-o', action='store_true', help='output game data as a csv')

    args = parser.parse_args()
    count = copy.deepcopy(args.count)

    totalTurns = 0
    totalSorrys = 0
    totalLostTurns = 0
    wins = {Y:0,G:0,R:0,B:0}

    start = time.time()
    while count:
        game = Game()
        while game.winner == None:
            game.playTurn()
        totalTurns += game.totalTurns
        totalSorrys += sum(game.sorryCount.values())
        totalLostTurns += sum(game.lostTurns.values())
        wins[game.winner] += 1

        if (args.count < 10 and not args.outputData):
            print 'Game Over! {} wins in {} ({}) turns!'.format(game.winner, game.totalTurns, game.totalTurns - sum(game.lostTurns.values())) 
            print game.board.pawns
            print 'Sorry! There were {} total \'Sorry\'s\'. {}'.format(sum(game.sorryCount.values()), game.sorryCount)
            print '{} total turns were skipped because there was not a valid move. {}'.format(sum(game.lostTurns.values()), game.lostTurns)
        count -= 1

        if args.outputData:
            for state in game.states:
                print state + ',' + str(game.winnerToInt())
    end = time.time()
    if args.count > 1 and not args.outputData:
        print 'Simulated {0} total games in {1:.2f} milliseconds. On average there were {2} ({4}) turns and {3} \'Sorry\'s\' per game.'.format(args.count, end-start, totalTurns/args.count, totalSorrys/args.count, totalLostTurns/args.count)
        print 'Wins: ' + str(wins)

if __name__ == "__main__":
    main()