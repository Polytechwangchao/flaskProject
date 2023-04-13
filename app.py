from flask import Flask, request, redirect, render_template, session
from gevent import pywsgi
from waitress import serve
app = Flask(__name__,static_folder='static', static_url_path='',template_folder='templates')

app.secret_key = 'QWERTYUIOP'  # 对用户信息加密
app._static_folder = "templates"

@app.route('/login', methods=["GET","POST"])  # 路由默认接收请求方式为POST，然而登录所需要请求都有，所以要特别声明。
def login():
    user = request.form.get('username')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd =='123':
        return render_template("监控系统.html")
    else:
        return render_template("login.html",msg="登录失败")
#text

@app.route('/')
def index():
   return render_template("login.html")




if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8080)
