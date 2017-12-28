__author__ = 'Yangyang'
#coding=utf8

import MySQLdb

class Mysql:
    host = 'localhost'
    port = 3306
    user = 'root'
    pwd  = 'pinpin123'
    # pwd  = '123'

    def __init__(self):

        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.pwd, db='test', port=self.port, charset='utf8')
        self.conn.set_character_set('utf8')
        self.cur = self.conn.cursor()

    # (id, cid, title,content, time, tag)
    def insertArticle(self, tablename, result):
        try:
            sql = 'insert into bloglist (id, cid, title, content, summary, mtime, tag) VALUE ("%d","%d","%s","%s","%s","%s","%s")' % result
            self.cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def selectAllFromTable(self,tableName):
        try:
            sql = 'select * from %s', tableName
            self.cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def searchData(self):
        try:
            sql = 'select * from blog'
            self.cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def executeSql(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])