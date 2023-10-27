from flask import Flask, render_template, request

app = Flask(__name__)

# Lista delle domande e risposte
questions = [
    {
        'question': 'Qual è la capitale dell'Italia?',
        'options': ['Roma', 'Milano', 'Firenze', 'Napoli'],
        'correct_answer': 'Roma'
    },
    {
        'question': 'Quale è il fiume più lungo del mondo?',
        'options': ['Nilo', 'Amazzoni', 'Mississippi', 'Danubio'],
        'correct_answer': 'Nilo'
    },
    {
        'question': 'Quale è il simbolo chimico dell\'oro?',
        'options': ['Au', 'Ag', 'Fe', 'Cu'],
        'correct_answer': 'Au'
    }
]

@app.route('/')
def index():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        user_answer = request.form.get(question['question'])
        if user_answer == question['correct_answer']:
            score += 1
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
