from random import shuffle
import copy
import itertools

Y = "Y"
G = "G"
R = "R"
B = "B"
PLAYERS = [Y,G,R,B]
OPPONENTS = {Y:[G,R,B], G:[Y,R,B], R:[Y,G,B], B:[Y,G,R]}
cards = [1,2,3,4,5,7,8,10,11,12,'sorry']
possibleSevenSplits = [[1,6],[2,5],[3,4]]

offsets = {Y:0,G:15,R:30,B:45}
safeZoneEntrance = 2
start = 4
smallSlideStarts = {1:Y,16:G,31:R,46:B}
largeSlideStarts = {9:Y,24:G,39:R,54:B}

class Board:
    def __init__(self):
        self.deck = shuffle(self.initDeck())
        self.discardPile = []
        self.pawns = {Y: ["start", "start", "start", "start"],
                      G: ["start", "start", "start", "start"],
                      R: ["start", "start", "start", "start"],
                      B: ["start", "start", "start", "start"],}  

    def drawCard(self):
        card = self.deck.pop()
        self.discardPile.append(card)

        if len(deck) == 0:
            self.deck = shuffle(self.discardPile)
            self.discardPile = []

        return card

    def setPawns(self, pawns):
        self.pawns = pawns

    def initDeck(self):
        deck = [1]
        for card in cards:
            for x in range(4):
                deck.append(card)
        return deck

    def getStartSpot(self, player):
        return 'board:' + str(start + offsets[player])

    def getSafeSpot(self, player):
        return safeZoneEntrance + offsets[player]

    def isSpotSlide(self, player, spotNumber):
        if spotNumber in smallSlideStarts and smallSlideStarts[spotNumber] != player:
            return 3
        if spotNumber in largeSlideStarts and largeSlideStarts[spotNumber] != player:
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

    def applySlide(self, player, newSpot, pawns):
        spotParts = newSpot.split(':')
        newSpot = spotParts[0]
        newSpotNumber = int(spotParts[1])

        slide = self.isSpotSlide(player, newSpotNumber)
        if (slide):
            while slide != 0:
                newSpotNumber += 1
                playerAtSpot = self.pawnAtLocation(pawns, newSpot+':'+str(newSpotNumber))
                if playerAtSpot:
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

            newSpotNumber = self.applySlide(player, newSpot+':'+str(newSpotNumber), pawns)
            if newSpotNumber == None:
                return None

        if (newSpot+':'+str(newSpotNumber)) in playerPawns:
            return None

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

class Game:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = Y
        self.winner = None

    def setPawns(self, pawns):
        self.board.setPawns(pawns)

    def playTurn(self):
        card = self.board.drawCard();
        possibleGameStates = computePossibleGameStates(card, currentPlayer, board)

    def computePossibleGameStates(self, card, player):
        possibleStates = []
        pawnsInPlay = self.board.pawnsInPlay(player)
        numPawnsAtStart = self.board.numPawnsAtStart(player)
        opponentPawnsInPlay = self.board.opponentPawnsInPlay(player)

        if ((card == 1 or card == 2) and numPawnsAtStart > 1):
            possibleStates.append(self.board.startPawn(player))
        
        if (card == 'sorry' and numPawnsAtStart > 1):
            for opponentPawn in opponentPawnsInPlay:
                possibleStates.append(self.board.sorry(player, opponentPawn))
        
        if (pawnsInPlay > 0):
            if (card == 7 and pawnsInPlay > 1):
                possibleCombinations = itertools.combinations(pawnsInPlay, 2)
                for pawnCombination in possibleCombinations:
                    for possibleSplit in possibleSevenSplits:
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

def main():
    game = Game()

if __name__ == "__main__":
    main()