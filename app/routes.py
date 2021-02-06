from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '李芳华'}
    title = '登录'
    posts = [
        {'author': {'username':'张飞'},
         'body': '测试测试测试测试'
         },
        {'author': {'username':'赵云'},
         'body': '测试测试测试测试'
         }
    ]
    return render_template('index.html', user=user, title=title,posts=posts)
