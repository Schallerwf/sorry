# Ultimate Sorry

Ultimate Sorry is a python application that can
1. Simulate games of Sorry 
2. Present a web UI for entering the state of a board and analyzing potential moves
3. Train a random forest model to play the game Sorry

In my experience playing sorry, moves are not always made on what best improves your position but instead what most hurts others. Alliances can form, relationships can sour, treachery can turn the tide. To simulate this, the AI players can be configured to be motivated by different things, themselves winning, someone else winning, or someone specific loosing. This helps simulate some interesting things, for example if you are too boastful and the rest of the board sets out to make you lose, can you still win? Chances are, no, you will probably lose. Even if one player makes it their mission to make you lose, your chance of winning drops to just 13%. 

To run the unit tests
`
python test_sorry.py
`

The simulate games of Sorry
`
python sorry.py
`

To run the web server
`
python server.py
`

~~View the web app here - https://ultimatesorry.herokuapp.com/~~ RIP Heroku
