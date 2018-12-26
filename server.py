from flask import Flask, render_template, request
app = Flask(__name__)

import json
import pickle

from sorry import analyzeBoard

RF_MODEL = pickle.load(open('ml/models/basic.rf', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        args = request.json
        pawns = args.get('pawns')
        card = args.get('card')
        player = args.get('player')
        return json.dumps(analyzeBoard(pawns, player, card, RF_MODEL))
    else:
        return render_template('setup_board.html')

if __name__ == '__main__':
    app.run()