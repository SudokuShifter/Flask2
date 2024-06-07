from flask import Flask, render_template, request, make_response, flash, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def main():
    context = {
        'title': ''
    }
    response = make_response(render_template('main.html', **context))
    response.set_cookie('username', 'Eliot')
    response.set_cookie('mail', 'MrRobot@yahoo.com')
    return response


@app.route('/authorize/', methods=['GET', 'POST'])
def authorize():
    context = {
        'title': 'Авторизация',
        'name': 'Введите Ваше имя',
        'mail': 'Введите электронную почту',
    }
    if request.method == 'POST':
        name = request.form.get('auth_name')
        mail = request.form.get('auth_email')
        response = make_response(redirect(url_for('authorize')))
        response.set_cookie('username', str(name))
        response.set_cookie('mail', str(mail))
        flash('Форма успешно отправлена!', 'success')
        return response
    return render_template('authorize.html', **context)


@app.route('/del_cookie/')
def del_cookie():
    context = {
        'title': 'Удаление куки'
    }
    response = make_response(render_template('del_cookie.html', **context))
    response.set_cookie('username', 'val', max_age=0)
    response.set_cookie('mail', 'val', max_age=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)