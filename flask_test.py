#-*- coding=utf-8 -*-
# coding=utf-8
# encoding:utf-8

from flask import Flask, render_template, json, url_for,send_file
from flask import request
from flask import current_app
from flask import redirect

from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootStrap = Bootstrap(app)

test = [{'time': '2017.7.1',
                'tag':   unicode('Python人单独','utf8'),
                'title': 'Python',
                'content': 'ddddsss'}]
article = [{    'id'  : '1',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈','utf8')},
               {'id'  : '2',
                'time': '2017.7.2',
                'tag': 'Python',
                'title': unicode('Python进阶','utf8'),
                'content': unicode('这是个神奇的语言，进阶了阿萨法画江湖公交卡进度款','utf8')},
               {'id'  : '3',
                'time': '2017.7.1',
                'tag': 'iOS',
                'title': unicode('iOS开发啊','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈','utf8')},
               {'id'  : '4',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈','utf8')},
               {'id'  : '5',
                'time': '2017.7.2',
                'tag': 'Python',
                'title': unicode('Python进阶','utf8'),
                'content': unicode('这是个神奇的语言，进阶了阿萨法画江湖公交卡进度款','utf8')},
               {'id'  : '6',
                'time': '2017.7.1',
                'tag': 'iOS',
                'title': unicode('iOS开发啊','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈','utf8')}
               ]

jsonData = json.dumps(article)


@app.route('/')

def index():
    # user_agent = request.headers.get('User-Agent')

    # app_ctx = app.app_context()
    # app_ctx.push()
    # print current_app.name
    # app_ctx.pop()

    # print app.url_map
    flagArray = [1,2,3,4,5,6,7]

    return render_template('newHome.html',articleArray=article)

@app.route('/queryArticle')
def queryArticle():


    return jsonData

@app.route('/queryTag/<tag>')
def queryArticleTag(tag):
    tagArticle = []

    for m in article:

        if(m['tag'] == tag):
            print ('%s == %s', m['tag'], tag)

            tagArticle.append(m)

    jsonTagArticle = json.dumps(tagArticle)

    return jsonTagArticle

@app.route('/sub')
def subArticle():
    return render_template('home_subArticle.html')

@app.route('/article')
def showArticle():

    myID = request.values.get('id')


    # articleContent = '<h1 class="blog-title">The Bootstrap Blog</h1>'
    # return redirect(url_for(".article"))
    # return send_file('/templates/article.html')
    return render_template('article.html',myID = myID)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/aaa')
def re():   #don't repeat name redirect that while cover this method in flask

    return redirect('/')

@app.route('/input')
def input():
    return render_template('post_article.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run(debug=True)
