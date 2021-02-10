from flask import render_template, request
from app import app, forms


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    user = {'username': '李芳华'}
    title = '登录'
    posts = [
        {'author': {'username': '张飞'},
         'body': '测试测试测试测试'
         },
        {'author': {'username': '赵云'},
         'body': '测试测试测试测试'
         }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)


@app.route('/login', methods=['GET'])
def login():
    form = forms.LoginForm(prefix='a')
    return render_template('login.html', title='登录', form=form)


@app.route('/login', methods=['POST'])
def loginSubmit():
    token = request.form['a-csrf_token']
    password = request.form['a-password']
    username = request.form['a-username']
    return username