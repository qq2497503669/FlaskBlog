from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '李芳华'}
    title = '登录'
    return render_template('index.html', user=user, title=title)
