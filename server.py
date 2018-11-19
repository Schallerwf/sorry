from flask import Flask, render_template, request
app = Flask(__name__)

from Sorry import analyzeBoard
import json

@app.route('/', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        args = request.json
        pawns = args.get('pawns')
        card = args.get('card')
        player = args.get('player')
        return str(analyzeBoard(pawns, player, card))
    else:
        return render_template('setup_board.html')

if __name__ == '__main__':
    app.run()