from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def phrase():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def ad():
    return '<br/>'.join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!',
                         'Присоединяйся!'])


@app.route('/image_mars')
def image():
    return """<h1>Жди нас, Марс!</h1>
    <img src='static/mars.jpg' width="400" height='250'>
    <p>Вот она какая, красная планета.</p>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
