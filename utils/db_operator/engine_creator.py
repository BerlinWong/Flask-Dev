#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 9:04
# @Author  : Berlin Wong
# @File    : engine_creator.py
# @Software: PyCharm
from utils import config
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


def init_db():
    username = config.get('mysql', 'MYSQL_USERNAME')
    password = config.get('mysql', 'MYSQL_PASSWORD')
    host = config.get('mysql', 'MYSQL_HOST')
    port = config.get('mysql', 'MYSQL_PORT')
    database = config.get('mysql', 'MYSQL_DATABASE')

    # 构建 MySQL 连接字符串
    db_connection_str = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"

    # 创建 SQLAlchemy 引擎
    engine = create_engine(db_connection_str)
    Session = sessionmaker(bind=engine)

    return engine, Session
