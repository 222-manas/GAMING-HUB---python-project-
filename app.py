from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-tic-tac-toe')
def start_tic_tac_toe():
    subprocess.Popen(['python', 'tic_tac_toe_game.py'])
    return "Tic-Tac-Toe game started!"

@app.route('/start-snake')
def start_snake():
    subprocess.Popen(['python', 'snake_game.py'])
    return "Snake game started!"

@app.route('/start-car-game')
def start_car_game():
    subprocess.Popen(['python', 'car_game.py'])
    return "Car game started!"

@app.route('/start-flappy-bird')
def start_flappy_bird():
    subprocess.Popen(['python', 'flappy_bird.py'])
    return "Flappy Bird game started!"

if __name__ == '__main__':
    app.run(port=5000)
