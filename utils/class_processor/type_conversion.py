#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 14:30
# @Author  : Berlin Wong
# @File    : sqlalchemy_class_to_dict.py
# @Software: PyCharm
from datetime import datetime

from loguru import logger


# 单表查询
# e.g. users = db.session.query(User).all()
def class_to_dict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            _dict = {}
            a = o.__dict__
            if "_sa_instance_state" in a:
                del a['_sa_instance_state']
            _dict.update(a)
            obj_arr.append(_dict)
        return obj_arr
    else:
        _dict = {}
        a = obj.__dict__
        if "_sa_instance_state" in a:
            del a['_sa_instance_state']
        _dict.update(a)
        return _dict


# 多表查询
# e.g. user_c = db.session.query(User,Comment).join(Comment).all()
def to_json_list(res):
    count = 0
    json_list = []
    _dict = {}
    for u in res:
        for c in u:
            count += 1
            if count <= len(u):
                _dict.update(class_to_dict(c))  # 函数class_to_dict
                if count == len(u):
                    json_list.append(_dict)
            else:
                count = 1
                _dict = {}
                _dict.update(class_to_dict(c))  # 函数class_to_dict


def join_select_first_to_json(res_tuple):
    dict_ = {}
    for item in res_tuple:
        dict_.update(format_datetime_recursive(class_to_dict(item)))
    return dict_


def join_select_all_to_json(res_list):
    list_ = []
    for tuple_container in res_list:
        dict_ = {}
        for i in tuple_container:
            dict_.update(format_datetime_recursive(class_to_dict(i)))
        list_.append(dict_)
    return list_


# 将GMT转换为年月日
def format_datetime_recursive(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = format_datetime_recursive(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            data[i] = format_datetime_recursive(item)
    elif isinstance(data, datetime):
        data = data.strftime('%Y-%m-%d %H:%M:%S')
    return data
