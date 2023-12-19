from flask import Flask, url_for, render_template, request, make_response, redirect

app = Flask(__name__)


@app.get('/')
def index():
    return render_template("email_form.html")


@app.post('/email_form')
def index_post():
    username = request.form.get("username")
    email = request.form.get("email")
    resp = make_response(render_template('name.html', context=username))
    resp.set_cookie(username, email)
    return resp


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    cookies = request.cookies
    for cookies_name in cookies:
        resp.set_cookie(cookies_name, '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
