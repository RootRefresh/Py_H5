# from sqlalchemy.types import *
# from sqlalchemy import Table, Column
# from sqlalchemy.orm import mapper
# from DBSession import metaData,db_session

# from DBSession import db_session as db
#
# class bloglist(db.Model):
#     __tablename__ = 'bloglist'
#
#     # query = db_session.query_property()
#
#     id = db.Column(db.INT(11), primary_key=True)
#     title = db.Column(db.VARCHAR(100))
#     summary = db.Column(db.TEXT)
#     mtime = db.Column(db.VARCHAR(100))
#     tag = db.Column(db.VARCHAR(45))
#     content = db.Column(db.TEXT)
#     cid = db.Column(db.INT(11))
#
#     def __init__(self,id,title,summary,mtime,tag,content,cid):
#         self.id = id
#         self.title = title
#         self.summary = summary
#         self.mtime = mtime
#         self.tag = tag
#         self.content = content
#         self.cid = cid
#
#     def __repr__(self):
#         return '<title %r>' % self.title
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()


# blog = Table('bloglist',metaData,
#         Column('id',INT(11), primary_key=True),
#         Column('title',VARCHAR(100)),
#         Column('summary',TEXT),
#         Column('mtime',VARCHAR(100)),
#         Column('tag',VARCHAR(45)),
#         Column('content',TEXT),
#         Column('cid',INT(11))
# )
# mapper(Blog,blog)

