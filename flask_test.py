from flask import Flask, render_template
from flask import request
from flask import current_app
from flask import redirect

from flask_bootstrap import Bootstrap



app = Flask(__name__)

bootStrap = Bootstrap(app)


@app.route('/')

def index():
    user_agent = request.headers.get('User-Agent')

    app_ctx = app.app_context()
    app_ctx.push()
    print current_app.name
    app_ctx.pop()

    print app.url_map
    flagArray = [1,2,3,4,5,6,7]
    return render_template('home.html',flagArray=flagArray)
@app.route('/sub')
def subArticle():
    return render_template('home_subArticle.html')

@app.route('/article')
def showArticle():
    return render_template('article.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/aaa')
def re():   #don't repeat name redirect that while cover this method in flask

    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run(debug=True)
