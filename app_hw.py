from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная страница'}
    return render_template('base.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Курткв'}
    return render_template('jacket.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/hi/')
def hi():
    return 'HI'

if __name__ == '__main__':
    app.run()