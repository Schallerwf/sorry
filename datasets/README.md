Each dataset consists of 10,000 simulated games. 8,000 for training, 2,000 for testing. The data is stored as a CSV where the first 16 values are the numarical positions of the pawns on the board, and the 17th value is the index of the winning player.

p0,p0,p0,p0,p1,p1,p1,p1,p2,p2,p2,p2,p3,p3,p3,p3,winner

A pawn position is an integer between 0 and 66. 0 being safe, 1-60 being on the board, 60-65 being in the safe zone, and 66 being home.

## basic
The games were played with each AI player using a basic selfish strategy

## random
The games were played with each AI player randomly selecting their move

## singleSmart
The games were played with 1 AI player (player 0) using a basic strategy and the rest (players 1, 2, and 3) randomly selecting their move
