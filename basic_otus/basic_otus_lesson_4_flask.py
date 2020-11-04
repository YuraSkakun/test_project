from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route('/')
def index_page():
    names_list = ['John', 'Jimm', 'Sara',]
    # return '<h1>Hello World!</h1>'
    return render_template('basic_otus_lesson_4_index.html', names=names_list)


@app.route('/hello/')
@app.route('/hello/<name>/')
def hello_page(name=None):
    # if not name:
    #     name = 'Page'
    # return f'<h2>Hello {name}</h2>'
    return render_template('basic_otus_lesson_4_hello.html', name=name)


@app.route('/article/')
@app.route('/article/<int:a_id>/')
def article_page(a_id=None):
    if a_id is None:
        # a_id = 1
        return redirect(url_for('article_page', a_id=1))
    return  render_template('basic_otus_lesson_4_article.html', a_id=a_id)


@app.route('/article/<string:a_id>/')
def article_page_str(a_id):
    return f'<h1>Nothing for Article "{a_id}"</h1>', 404


@app.route('/user/', methods=['GET', 'POST'])
def user_page():
    # print(request)
    # return f'Hello user! {request}'
    # return render_template('basic_otus_lesson_4_user.html', request=vars(request))
    if request.method == 'POST':
        print(request.form)
        # return f'<h3>USER NAME: {request.form.get("fname", "not stated")}</h3>'
        user_name = request.form['fname']
        if not user_name:
            user_name = 'not stated'
        return f'<h3>USER NAME: {user_name}</h3>'
    return render_template('basic_otus_lesson_4_user.html')


if __name__ == '__main__':
    # app.run(host='localhost', port=5000)
    app.run(host='localhost', port=5000, debug=True)
