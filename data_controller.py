import mysql

def searchArticleList():

    db = mysql.Mysql()

    db.selectAllFromTable('bloglist')

    data = db.cur.fetchall()

    print data

    db.conn.close()

    return ''