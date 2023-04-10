from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)

app.secret_key = 'QWERTYUIOP'  # 对用户信息加密


@app.route('/login', methods=["GET","POST"])  # 路由默认接收请求方式为POST，然而登录所需要请求都有，所以要特别声明。
def login():
    user = request.form.get('username')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd =='123':
        return render_template("监控系统.html")
    else:
        return render_template("login.html",msg="登录失败")


@app.route('/')
def index():
   return render_template("login.html")




if __name__ == "__main__":
    app.run(debug=True)
