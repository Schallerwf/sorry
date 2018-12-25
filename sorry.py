import argparse
from collections import Counter
import copy
import sys
import time

from board import Board
from game import Game
from sorry_constants import *
from strategy import Strategy
from util import *

def analyzeBoard(currentGameState, currentPlayer, currentCard):
    currentGameState = capitalize_keys(currentGameState)
    currentCard = int(currentCard) if currentCard.isdigit() else currentCard
    game = Game()
    game.setPawns(currentGameState)
    possibleGameStates = game.computePossibleGameStates(currentCard, currentPlayer)

    gameStates = []
    for possibleGameState in possibleGameStates:
        gameStates.append({'gameState': possibleGameState,
                           'distances': game.board.totalDistances(possibleGameState)})

    results = {'inputState': {'distances': game.board.totalDistances(currentGameState)},
               'possibleGameStates': gameStates}

    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', '-c', default=1, type=int, help='number of sorry games to simulate. defaults to 1')
    parser.add_argument('--outputData', '-o', default=False, action='store_true', help='output game data as a csv')

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