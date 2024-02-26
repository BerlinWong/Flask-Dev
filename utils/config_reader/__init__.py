#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/18 16:58
# @Author  : Berlin Wong
# @File    : __init__.py.py
# @Software: PyCharm

from .ConfigReader import ConfigReader

from loguru import logger
import os

__all__ = ['config']

# 获取当前工作目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 定义相对于当前工作目录的配置文件路径
# config_path = os.path.join(current_dir, 'config_dev.ini')
# logger.info(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
# logger.info(os.path.join(config_path, 'config'))

current_script_directory = os.path.abspath(os.path.dirname(__file__))

# 找到config目录的路径
config_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..', 'config'))

config_path = os.path.join(config_directory, 'config_dev.ini')
logger.debug("The current profile: " + config_path)

# 提供一个方法来获取 ConfigReader 实例
config = ConfigReader(config_path).config
