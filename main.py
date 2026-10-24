import random

from flask import Flask, redirect, render_template, session, url_for

f = Flask(__name__)
f.secret_key = 'н#е3фтЕ-9югА5нс№к_5%4!3'

QUESTIONS = [
    {
        'text': 'Появились машины, отопление, энергию нужно добывать. Казалось бы что это - круто! А что делать? Как их заправлять?',
        'choices': ['Добывать нефть','Добывать уголь', 'Сделать солнечные батареи', 'Не выпускать ничего из этого', 'Пробить дно машины и ездить на ногах или сделать педали, отопление не делать, а делать пледы, поставить ветрянные мельницы'],
        'answer': 2
    },
    {
        'text': 'Нужна древесина: для бумаги, мебели и т.д.',
        'choices': ['Вырубать леса','Вырубать леса и садить деревья', 'Заранее садить деревья, а потом вырубать леса', 'Заменить древесину пластииком', 'Забить на потребность жителей'],
        'answer': 2
    },
    {
        'text': 'Свалки. Что делать?',
        'choices': ['Ну валяется мусор и валяется. Что сделать?. Ничего', 'Поставить сортировку мусора, а пищевые удобрения на переработку', 'Сжигать мусор', 'Поставить сортировку мусора, а пищевые удобрения на переработку. Но ещё добавить профессию, которая будет проверять отходы, чтобы не правильные отходы не попали куда не нужно'],
        'answer': 3
    },
    {
        'text': 'Промышленные процессы. Ну цемент и что? Ну сталь и что? Ну электроника и что? Ну товары и что?',
        'choices': ['Сокращать отходы, перейти на возобнавляемую энергию', 'Забросить заводы', 'Ничего не делать, так как всё это нужно'],
        'answer': 0
    },
    {
        'text': 'Сельское хозяйство и животноводство. Казалось бы: вроде ничего такого, да?',
        'choices': ['Ну да, ничего такого. А как тогда производить продукты?. Оставляем', 'Не заниматься больше этим', 'Попробывать делать всё это эколоогичней: природные удобрения, органическое земляделие, рациональное использование земли, более экологичный корм, улучшение ухода'],
        'answer': 2
    }
]

@f.route('/')
def index():
    return render_template('index.html')


@f.route('/start')
def start():
    session['score'] = 0
    order = list(range(len(QUESTIONS)))
    random.shuffle(order)
    session['order'] = order
    return redirect(url_for('next_question'))
    #return redirect(url_for('question', qid=random.randint(0, len(QUESTIONS)-1)))


@f.route('/question/<int:qid>')
def question(qid):
    if 0 <= qid < len(QUESTIONS):
        return render_template('question.html', q=QUESTIONS[qid], qid=qid)
    return redirect(url_for('index'))


@f.route('/answer/<int:qid>/<int:choice>')
def answer(qid, choice):
    if choice == QUESTIONS[qid]['answer']:
        session['score'] += 1
        return render_template('answer.html', correct=True, score=session['score'])
    else:
        return render_template('answer.html', correct=False, score=session['score'])
    #return redirect(url_for('next_question'))


@f.route('/next')
def next_question():
    order = session['order']
    if not order:
        return redirect(url_for('result'))
    qid = order.pop(0)
    session['order'] = order
    return redirect(url_for('question', qid=qid))


@f.route('/result')
def result():
    return render_template('result.html', score=session['score'], total=len(QUESTIONS))


f.run(debug=True)