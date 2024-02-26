#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/15 14:28
# @Author  : Berlin Wong
# @File    : ConfigReader.py
# @Software: PyCharm

import configparser


class ConfigReader:
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

        # 在初始化时加载配置项
        self.load_sections(['network_interface'])

    def load_sections(self, sections):
        for section in sections:
            for option in self.config.options(section):
                option_value = self.config.get(section, option)
                setattr(self, option, option_value)
