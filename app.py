from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

quiz = [
    {
        'id': 1,
        'question': 'Столица Франции?',
        'options': ['Париж', 'Лондон', 'Берлин', 'Рим'],
        'answer': 'Париж'
    },
    {
        'id': 2,
        'question': 'Какой язык используется для разработки Flask?',
        'options': ['Java', 'Python', 'C#', 'PHP'],
        'answer': 'Python'
    },
    {
        'id': 3,
        'question': '2 + 2 = ?',
        'options': ['3', '4', '5', '6'],
        'answer': '4'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    score = None
    if request.method == 'POST':
        score = 0
        for q in quiz:
            user_answer = request.form.get(f"question_{q['id']}")
            if user_answer == q['answer']:
                score += 1
    return render_template('main.html', quiz=quiz, score=score)

if __name__ == '__main__':
    app.run(debug=True)