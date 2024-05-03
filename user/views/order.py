from flask import Blueprint,session, redirect, render_template
from utile import db

od = Blueprint("order", __name__)

@od.route('/order/list')
def order_list():
    user_info = session.get("user_info")
    username = user_info['username']
    print(user_info, type(user_info))
    data_list = db.fetch_all("select * from order", [])

    return render_template('order.htnl')

@od.route('/order/create')
def order_create():

    return "创建订单"

@od.route('/order/delete')
def delete_list():

    return "删除订单"