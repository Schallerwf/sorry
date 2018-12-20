from flask import Flask, render_template, request
app = Flask(__name__)

import json
from sorry import analyzeBoard

@app.route('/', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        args = request.json
        pawns = args.get('pawns')
        card = args.get('card')
        player = args.get('player')
        return json.dumps(analyzeBoard(pawns, player, card))
    else:
        return render_template('setup_board.html')

if __name__ == '__main__':
    app.run()