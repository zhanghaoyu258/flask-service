from flask import Blueprint, request, render_template, redirect, session
from utile import db
import pymysql
#蓝图对象
ac = Blueprint("account", __name__)

@ac.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    print(username,password)

    user_dict = db.fetch_one("select * from user where username=%s and password=%s",[username,password])
    if user_dict:
        session["user_info"] = {"username": user_dict['username'], "pwd": user_dict['password']}
        return redirect('/order/list')
    return  render_template("login.html",error="用户名或密码错误")

@ac.route('/user')
def user():

    return "用户"