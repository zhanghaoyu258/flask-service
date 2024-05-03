from flask import Flask, request,session, redirect

app = Flask(__name__)

def auth():
    if request.path.startswith("/static"):
        return

    if request.path == '/login':
        #继续向后执行，不拦截
        return
    user_info = session.get("user_ingo")
    if user_info:
        #继续向后执行
        return
    return redirect('/login')

def create_app():
    app = Flask(__name__)
    app.secret_key = 'adsaobdn'

    from .views import account
    from .views import order
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    app.before_request(auth)
    return app