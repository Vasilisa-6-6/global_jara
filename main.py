import random
from flask import Flask, render_template, session, redirect, url_for

f = Flask(__name__)
f.secret_key = 'н#е3фтЕ-9югА5нс№к_5%4!3'

QUESTIONS = [
    {
        'text': 'Появились машины. Казалось бы что это - круто! А что делать? Как их заправлять?',
        'choices': ['Добывать нефть и делать бензин','Добывать уголь и делать электро-машины', 'Сделать на машинах солнечные батареи', 'Не выпускать машины', 'Пробить дно машины и ездить на ногах или сделать педали'],
        'answer': 2
    }
]

@f.route('/')
def index():
    return render_template('index.html')


@f.route('/start')
def start():
    session['score'] = 0
    return redirect(url_for('question', qid=random.randint(0, len(QUESTIONS)-1)))

@f.route('/question/<int:qid>')
def question(qid):
    if 0 <= qid < len(QUESTIONS):
        return render_template('question.html', q=QUESTIONS[qid])

f.run(debug=True)