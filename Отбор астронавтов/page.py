from flask import Flask, url_for

app = Flask(__name__)


@app.route('/astronaut_selection')
def astronaut_selection():
    return """
        <!DOCTYPE html>
        
        <html>
            <head>
                <title>Регистрация</title>
                <link rel='stylesheet' href='{}'>
            </head>
        
            <body>
                <h1>Анкета претендента</h1>
                <h2>на участие в миссии</h2>
                <form>
                    <div class='form_element'><input type='text' required placeholder='Введите фамилию' for='lastname'></div>
                    <div class='form_element'><input type='text' required placeholder='Введите имя' for='firstname'></div>
                    <div class='form_element more_space'><input type='text' required placeholder='Введите адрес почты'></div>
                    
                    <div class='form_element more_space'>
                        <div><label for='education'>Какое у вас образование?</label></div>
                        <div><select name='education'>
                            <option value='Начальное'>Начальное</option>
                            <option value='Среднее'>Среднее</option>
                            <option value='Высшее'>Высшее</option>
                        </select></div>
                    </div>
                    
                    <div class='form_element more_space'>
                        <label for='job'>Какие у вас были профессии?</label>
                        <br>
                        
                        <div>
                        <input type='checkbox' id='пилот'>
                        <label for='пилот'>Пилот</label>
                        </div>
                        
                        <div>
                        <input type='checkbox' id='строитель'>
                        <label for='строитель'>Строитель</label>
                        </div>
                        
                        <div>
                        <input type='checkbox' id='врач'>
                        <label for='врач'>Врач</label>
                        </div>
                    </div>
                    
                    <div class='form_element more_space'>
                        <div><label for='sex'>Пол</label></div>
                    	<label>
					    	<input type="radio" name="sex" value="мужской">мужской
					    </label>
					    <label>
					    	<input type="radio" name="sex" value="женский">женский
					    </label>
					</div>

					<div class='form_element more_space'>
						<div><label for='will'>Почему вы хотите принять участие в миссии?</label></div>
						<div><input type='textarea' id='will'></div>
					</div>

					<div class='form_element more_space'>
						<div><label for='ready'>Готовы ли остаться на Марсе?</label></div>
						<div><input type='checkbox' id='ready'></div>
					</div>
                </form>
            </body>
        </html>
    """.format(url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
