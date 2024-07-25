from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        P1 = request.form.get('choice').strip().lower()
        
        # Validate Player 1 input
        if P1 not in ["kulob", "hayang"]:
            error_message = "Invalid choice. Please enter 'kulob' or 'hayang'."
            return render_template('index.html', error=error_message)
        
        choices = ["kulob", "hayang"]
        C2 = random.choice(choices)
        C3 = random.choice(choices)
        
        kulob_count = [P1, C2, C3].count("kulob")
        hayang_count = [P1, C2, C3].count("hayang")
        
        # Determine the unique choice and the winner
        if kulob_count == 1 and hayang_count == 2:
            winner = "Kulob wins!"
        elif hayang_count == 1 and kulob_count == 2:
            winner = "Hayang wins!"
        else:
            winner = "It's a tie!"

        return render_template('index.html', P1=P1, C2=C2, C3=C3, winner=winner)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
