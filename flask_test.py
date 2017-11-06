#-*- coding=utf-8 -*-
# coding=utf-8
# encoding:utf-8

from flask import Flask, render_template, json, url_for,send_file
from flask import request,jsonify
from flask import current_app
from flask import redirect

from flask_bootstrap import Bootstrap
import mysql,os,sys,time,data_controller


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = sys.path[0]+os.sep+"static"+os.sep+'img'
# sys.path[0]+os.sep+"static"+os.sep+'images'    //配置图片上传路径：./static/images/

bootStrap = Bootstrap(app)

test = [{'id'  : '100',
         'cid' : '100',
         'time': '2017.7.1',
                'tag':   unicode('Python人单独','utf8'),
                'title': 'Python',
                'content': 'ddddsss'}]
article = [{    'id'  : '0',
                'cid'  : '0',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈1','utf8')},

              {    'id'  : '1',
                'cid'  : '1',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门','utf8'),
                'content': unicode('<h1><span style="background-color: rgb(255, 255, 255);">标题</span></h1><p>这是文章正文测试</p><pre>code在这里</pre><blockquote>引用在这</blockquote><p><br></p>','utf8')},
               {'id'  : '2',
                'cid'  : '2',
                'time': '2017.7.2',
                'tag': 'Python',
                'title': unicode('Python进阶','utf8'),
                'content': unicode('这是个神奇的语言，进阶了阿萨法画江湖公交卡进度款3','utf8')},
               {'id'  : '3',
                'cid'  : '0',
                'time': '2017.7.1',
                'tag': 'iOS',
                'title': unicode('iOS开发啊','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈iOS1111','utf8')},
               {'id'  : '4',
                'cid'  : '3',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈55555','utf8')},
               {'id'  : '5',
                'cid'  : '4',
                'time': '2017.7.2',
                'tag': 'Python',
                'title': unicode('Python进阶','utf8'),
                'content': unicode('这是个神奇的语言，进阶了阿萨法画江湖公交卡进度款6666','utf8')},
               {'id'  : '6',
                'cid'  : '1',
                'time': '2017.7.1',
                'tag': 'iOS',
                'title': unicode('iOS开发啊','utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈iOS22222','utf8')},
               {'id': '7',
                'cid'  : '5',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门', 'utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈888', 'utf8')},
               {'id': '8',
                'cid'  : '6',
                'time': '2017.7.1',
                'tag': 'Python',
                'title': unicode('Python入门', 'utf8'),
                'content': unicode('这是个神奇的语言，我们要哈哈哈学哈哈哈哈9999', 'utf8')},
               ]

jsonData = json.dumps(article)
jsonData2 = json.dumps(test)


@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')

    # app_ctx = app.app_context()
    # app_ctx.push()
    # print current_app.name
    # app_ctx.pop()

    # print app.url_map

    # data_controller.searchArticleList()

    tag = request.values.get('tag')

    mArticle = []

    if tag != "" and tag != None:

        for m in article:

            if (m['tag'] == tag):
                print ('%s == %s', m['tag'], tag)

                mArticle.append(m)
        mArticle = mArticle[0:6]
    else:
        mArticle = article[0:6]

    return render_template('newHome.html', articleArray=mArticle)

@app.route('/queryArticle')
def queryArticle():

    mID = request.values.get('id')

    currentPage = request.values.get('currPage')
    currentPage = int(currentPage)
    tag = request.values.get('tag')

    mArticle = []

    if tag == '':
        # if len(article) > (currentPage-1)*6:
        if (len(article)-(currentPage-1)*6) >= 6:
            mArticle = article[(currentPage-1)*6:6]
        else:
            mArticle = article[(currentPage-1)*6:]

        return json.dumps(mArticle)

    else:
        for m in article:
            if m['tag'] == tag:
                mArticle.append(m)
        if (len(mArticle) - (currentPage-1)*6) >= 6:
            mArticle = mArticle[(currentPage-1)*6:6]
        else:
            mArticle = mArticle[(currentPage-1)*6:]

        return json.dumps(mArticle)

@app.route('/queryTag')
def queryArticleTag():

    tag = request.values.get('tag')


    tagArticle = []

    if tag != '':
        for m in article:

            if(m['tag'] == tag):
                print ('%s == %s', m['tag'], tag)

                tagArticle.append(m)
    else:

        tagArticle = article


    jsonTagArticle = json.dumps(tagArticle)

    return jsonTagArticle

@app.route('/sub')
def subArticle():
    return render_template('home_subArticle.html')

@app.route('/article')
def showArticle():

    myID = request.values.get('id')
    mTag = request.values.get('tag')
    result = []
    for m in article:
        if m['id'] == myID:
            result = m


    db = mysql.Mysql()

    db.searchData()
    dic = {}
    rData = db.cur.fetchall()
    for item in rData:
        dic = {'m':item}
    print rData
    print dic['m']
    print rData[0][1]
    r = decode(rData[0][1])


    print rData

    db.conn.close()

    # return redirect(url_for(".article"))
    # return send_file('/templates/article.html')

    return render_template('article.html', article=r, mTag=mTag)

@app.route('/queryCID')
def queryCID():

    mID = request.values.get('id')

    result = {}

    for m in article:
        if m['id'] == mID:
            result['cid'] = m['cid']

    return json.dumps(result)

@app.route('/articlePaging')
def paging():

    myCID = request.values.get('cid')

    tag = request.values.get('tag')

    isNext = bool(request.values.get('next'))

    index = int(request.values.get('index'))



    tmpArr = []

    result = {}

    if tag != '' and tag != 'null':

        # flag = 0
        for m in article:
            if m['tag'] == tag:
                tmpArr.append(m)
                # if m['cid'] == myCID:
                #     if isNext:
                #       index = flag + 1
                #     else:
                #       index = flag - 1
            # flag += 1

        if index < 0 or index > (len(tmpArr)-1):
            return ''

        result = tmpArr[index]

    else:

        if index < 0 or index > (len(article)-1):
            return ''

        result = article[index]
        # flag = 0
        # for m in article:
        #     if m['id'] == myID:
        #         if isNext:
        #             flag += 1
        #             break
        #         else:
        #             flag -= 1
        #             break
        #
        # result = article[flag]

    return json.dumps(result)
@app.route('/uploadImage',methods=['GET','POST'])
def uploadImage():
    if 'image_up' not in request.files:
        return jsonify(message='no pic')
    file_metas = request.files['image_up']
    filename = file_metas.filename
    file_metas.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return jsonify(message='success',url = '../static/img/{0}'.format(filename))
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
@app.route('/postArticle',methods=['GET','POST'])
def postArticle():
    print 'aaaaa#####'

    # data = request.get_data()
    # data = request.form.get('blog')

    data1 = request.get_json()

    title = data1['title']
    blog = encode(data1['blog'])
    nowTime = time.strftime('%Y.%m.%d %H:%M', time.localtime(time.time()))
    tag = data1['tag']

    new_article = (title, blog, nowTime, tag)

    db = mysql.Mysql()

    db.insertArticle('blog', new_article)

    db.conn.close()

    return 'success!!!!'

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
