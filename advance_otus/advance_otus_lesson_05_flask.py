from flask import Flask, request, render_template
from werkzeug.exceptions import NotFound

from products_views import products_app
from cart_views import cart_app


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products/')
app.register_blueprint(cart_app, url_prefix='/cart/')


'''
# @app.route('/', methods=['GET', 'POST', 'PUT'])
@app.route('/')
def index_page():
    if request.method == 'GET':
        # return 'Hello, World!'
        # return '<h1>Hello, World!</h1>'
        # response = render_template('index.html', name='OTUS')
        response = render_template('index.html', name='<s>OTUS</s>', spam='{{ name }}')
        return response
    return  f'Hello {request.method} request!'
'''

'''
@app.route('/')
def index_page():
    if request.method == 'GET':
        print(request)
        response = render_template(
            'index.html',
            name='<s>OTUS</s>',
            products=['spam', 'eggs'],
            args=request.args,
        )
        return response
    return  f'Hello {request.method} request!'
'''


# @app.route('/<string:name>')
@app.route('/')
@app.route('/<name>/')
@app.route('/<int:user_id>/')
@app.route('/<float:user_id>/')
def index_page(name=None, user_id=None):
    # a = 42
    # b = 0
    # a / b
    print(request)
    response = render_template(
        'index.html',
        # name=name if name else "World",
        name=name or "World",
        user_id=user_id,
    )
    return response



@app.route('/404/')
def not_found():
    raise NotFound


app.run('localhost', 8080, debug=True)
