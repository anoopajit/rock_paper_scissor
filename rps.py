from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = get_result(player_choice, computer_choice)
    return render_template('result.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

def get_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'You win!'
    else:
        return 'You lose!'

if __name__ == '__main__':
    app.run(debug=True)