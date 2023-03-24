from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)

app.secret_key = 'QWERTYUIOP'  # 对用户信息加密


@app.route('/login', methods=["POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
    user = request.form.get('username')
    pwd = request.form.get('pwd')
    if user == 'alex' and pwd == '123':  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        return "成功"
    else:
        return render_template("login.html",msg="登录失败")


@app.route('/')
def index():
   return render_template("login.html")




if __name__ == "__main__":
    app.run(debug=True)
