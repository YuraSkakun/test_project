from flask import Blueprint

cart_app = Blueprint('cart_app', __name__)


@cart_app.route('/')
def cart_page():
    return '<h1>CART</h1>'

@cart_app.route('/pay/')
def pay_page():
    return f'<h1>PAY</h1>'
