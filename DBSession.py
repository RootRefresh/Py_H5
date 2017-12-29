# from sqlalchemy import create_engine,MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('mysql://root:pinpin123@127.0.0.1:3306/test')
# metaData = MetaData()
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()

# def init_db():
#     metaData.create_all(bind=engine)
    # Base.metadata.create_all(bind=engine)

#!/usr/bin/python
#-*- coding=utf-8 -*-
# coding=utf-8
# encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pinpin123@127.0.0.1:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db_session = SQLAlchemy(app)



