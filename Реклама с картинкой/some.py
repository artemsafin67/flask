from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def phrase():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def ad():
    return


@app.route('/promotion_image')
def image():
    return """<!doctype html>
    <html>
        <head>
            <link rel="stylesheet" 
            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
            crossorigin="anonymous">
            <link rel='stylesheet' href={}>
            <title>Марс</title>
        </head>
        
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src='{}' width="400" height='250'>
            <div class="alert alert-primary">
                <br/>Человечество вырастает из детства.
                <br/>Человечеству мала одна планета.
                <br/>Мы сделаем обитаемыми безжизненные пока планеты.
                <br/>И начнем с Марса!
                <br/>Присоединяйся!
            </div>
        </body>
    </html>""".format(url_for('static', filename='css/style.css'), url_for('static', filename='mars.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
