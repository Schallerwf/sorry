import copy
import random

from sorry_constants import *

class Board:
    def __init__(self):
        self.deck = self.initDeck()
        self.discardPile = []
        self.pawns = {Y: ["start", "start", "start", "start"],
                      G: ["start", "start", "start", "start"],
                      B: ["start", "start", "start", "start"],
                      R: ["start", "start", "start", "start"],}

    def initDeck(self):
        deck = []
        for card in CARDS:
            for x in range(4):
                deck.append(card)
        random.shuffle(deck)
        return deck

    def toArray(self, pawns=None):
        if (pawns == None):
            pawns = self.pawns
        result = []
        for player in PLAYERS:
            playersPawns = pawns[player]
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
        for player, locations in pawns.items():
            for location in locations:
                if targetLocation == location:
                    return player
        return None

    def totalDistance(self, player, playersPawns, weights={}):
        result = 0
        for pawn in playersPawns:
            tmp = result
            if pawn == 'start':
                result += weights.get('start', 0)
            elif pawn == 'home':
                result += weights.get('home', 66)
            elif 'safe' in pawn:
                result += weights.get('safe', 60)
                result += int(pawn.split(':')[1])
            else:
                spot = (int(pawn.split(':')[1]) - PLAYER_OFFSETS[player] - 2) % 60
                if (spot == 0):
                    spot = 60
                result += spot
        return result

    def totalDistances(self, pawns, weights={}):
        distances = {}
        for player in PLAYERS:
            playersPawns = pawns[player]
            distances[player] = self.totalDistance(player, playersPawns, weights)
        return distances

    def rfScores(self, pawns, rfModel):
        predictions = rfModel.predict_proba([self.toArray(pawns)])[0]
        return {Y: predictions[0],
                G: predictions[1],
                R: predictions[2],
                B: predictions[3],}