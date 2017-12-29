#-*- coding=utf-8 -*-
# coding=utf-8
# encoding:utf-8

from flask import Flask, render_template, json, url_for,send_file
from flask import request,jsonify
from flask import current_app
from flask import redirect

from flask_bootstrap import Bootstrap
import mysql,os,sys,time,data_controller

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = sys.path[0]+os.sep+"static"+os.sep+'img'
# sys.path[0]+os.sep+"static"+os.sep+'images'    //配置图片上传路径：./static/images/

bootStrap = Bootstrap(app)

firstEnter = 0
nArticles = []

#ORM
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pinpin123@127.0.0.1:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    __tablename__ = 'bloglist'

    # query = db_session.query_property()

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    summary = db.Column(db.TEXT)
    mtime = db.Column(db.VARCHAR(100))
    tag = db.Column(db.VARCHAR(45))
    content = db.Column(db.TEXT)
    cid = db.Column(db.Integer)

    def __init__(self,id,title,summary,mtime,tag,content,cid):
        self.id = id
        self.title = title
        self.summary = summary
        self.mtime = mtime
        self.tag = tag
        self.content = content
        self.cid = cid

    # def __repr__(self):
    #     return '<title %r>' % self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

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

    mArticle  = []
    global firstEnter
    if firstEnter == 0:
        del nArticles[:]

        # db_session.create_all()
        # one = Blog('4','tiel','info','2017','tag','content','cid')
        # db_session.session.add(one)
        # db_session.session.commit()

        c = Blog.query.all()
        print c

        for blog in c :
            print blog.title
            print blog.content
            print blog.summary
            print blog.mtime
            
        db = mysql.Mysql()

        db.executeSql('select * from bloglist')

        rData = db.cur.fetchall()

        for item in rData:
            content = decode(item[5])
            desc    = item[2]
            dic = {'id':item[0],'title':item[1],'desc':desc,'time':item[3],'tag':item[4],'content':content,'cid':item[6]}
            nArticles.append(dic)

        db.conn.close()

    firstEnter += 1

    if tag != "" and tag != None:

        for m in nArticles:

            if (m['tag'] == tag):
                print ('%s == %s', m['tag'], tag)

                mArticle.append(m)
        mArticle = mArticle[0:6]
    else:
        mArticle = nArticles[0:6] #article[0:6]

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
        if (len(nArticles)-(currentPage-1)*6) >= 6:
            mArticle = nArticles[(currentPage-1)*6:6]
        else:
            mArticle = nArticles[(currentPage-1)*6:]

        return json.dumps(mArticle)

    else:
        for m in nArticles:
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
        for m in nArticles:

            if(m['tag'] == tag):
                print ('%s == %s', m['tag'], tag)

                tagArticle.append(m)
    else:

        tagArticle = nArticles


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

    for m in nArticles:
        if m['id'] == int(myID):
            result = m
            break


    # db = mysql.Mysql()
    #
    # db.searchData()
    # dic = {}
    # rData = db.cur.fetchall()
    #
    # for item in rData:
    #     dic = {'m':item}
    # print rData
    # print dic['m']
    # print rData[0][1]
    # r = decode(rData[0][1])
    #
    # print rData
    #
    # db.conn.close()

    # return redirect(url_for(".article"))
    # return send_file('/templates/article.html')

    return render_template('article.html', article=result['content'], mTag=mTag)

@app.route('/queryCID')
def queryCID():

    mID = request.values.get('id')

    result = {}

    for m in nArticles:
        if m['id'] == int(mID):
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
        for m in nArticles:
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

        if index < 0 or index > (len(nArticles)-1):
            return ''

        result = nArticles[index]
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
    info = data1['info']
    nowTime = time.strftime('%Y.%m.%d %H:%M', time.localtime(time.time()))
    tag = data1['tag']

    db = mysql.Mysql()
    db.executeSql('select * from bloglist')

    rData = db.cur.fetchall()

    maxID  = 0
    maxCID = 0
    for item in rData:

        if item[0] > maxID:
            maxID = item[0]
        if item[4] == tag:
            if item[6] > maxCID:
                 maxCID = item[6]


    new_article = (maxID+1, maxCID+1, title, blog, info, nowTime, tag)

    db.insertArticle('blog', new_article)

    db.conn.close()
    global firstEnter
    firstEnter = 0
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
