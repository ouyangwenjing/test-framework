#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
import logging


# # config 配置文件读取器
# class ConfigReader:
#
#     def read(self, module):
#         """
#         读取 ini 配置文件
#         :param module: 配置文件的模块参数
#         :return: 返回具体某个参数的值
#         """
#         # 配置文件路径
#         self.config_absolute_path = os.path.abspath(os.path.dirname(__file__))[
#                                     :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
#                                         "python-ui-auto-test")] + '/ui-test/resource/config/config.ini'
#         # 创建配置文件管理者
#         self.config_manager = configparser.ConfigParser()
#         # 以 utf-8 编码方式读取配置文件
#         self.config_manager.read(self.config_absolute_path, encoding='UTF-8')
#         # 返回读取配置文件内容字典
#         return dict(self.config_manager.items(module))
#
#     # 返回配置文件的绝对路径
#     def get_config_absolute_path(self):
#         return self.config_absolute_path
#
#
# # 检测 config 配置文件读取器
# if __name__ == "__main__":
#     # 输出 [driver] 中的数据
#     print(ConfigReader().read("driver"))

# 使用相对目录确定文件位置
_conf_dir = os.path.dirname(os.path.dirname(__file__)) + "/resource/config"
# print(_conf_dir)
_conf_file = os.path.join(_conf_dir,'config.ini')
# print(_conf_file)


# 继承ConfigParser，写一个将结果转为dict的方法
class MyParser(ConfigParser):

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d


# 读取所有配置，以字典方式输出结果
def _get_all_conf():
    _config = MyParser()
    result = {}
    if os.path.isfile(_conf_file):
        try:
            _config.read(_conf_file, encoding='UTF-8')
            result = _config.as_dict()
        except OSError:
            raise ValueError("Read config file failed: %s" % OSError)
    return result


# 将各配置读取出来，放在变量中，后续其它文件直接引用这个这些变量
config = _get_all_conf()
log = config['log']
# print(log)
