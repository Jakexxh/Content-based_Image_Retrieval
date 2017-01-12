from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin_form():
    return render_template('result.html')


@app.route('/', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
