from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "dodgeball_game_key"

@app.route('/')
def index():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)