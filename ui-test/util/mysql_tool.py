#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql as pymysql

from util.config_reader import config


# mysql 连接工具
class MysqlTool:
    # 初始化 mysql 连接
    def __init__(self):
        # mysql_ip
        self.host = config['mysql']["mysql_ip"]
        # mysql_port
        self.port = int(config['mysql']["mysql_port"])
        # mysql_db
        self.db = config['mysql']["mysql_db"]
        # mysql_user
        self.user = config['mysql']["mysql_user"]
        # mysql_pwd
        self.passwd = config['mysql']["mysql_pwd"]
        # mysql_charset
        self.charset = config['mysql']["mysql_charset"]
        # mysql 连接
        self.mysql_conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
                                          port=self.port, charset=self.charset)

    # execute 任何操作
    def execute(self, sql):
        """
        执行 sql 语句
        :param sql: sql 语句
        :return: select 语句返回
        """
        # 从 mysql 连接中获取一个游标对象
        cursor = self.mysql_conn.cursor()
        # sql 语句执行返回值
        ret = None
        try:
            # 执行 sql 语句
            ret = cursor.execute(sql)
            # a = cursor.fetchone()
            # for i in range(a[0]):
            #     aa, ab = cursor.fetchone()
            #     print(aa, ab)
            # 提交
            self.mysql_conn.commit()
        except Exception as e:
            # 异常回滚数据
            self.mysql_conn.rollback()
        # 关闭游标
        cursor.close()
        # 返回
        return format(ret)

    # 获取 mysql 连接
    def get_mysql_conn(self):
        return self.mysql_conn

    # mysql 连接释放
    def release_mysql_conn(self):
        if self.mysql_conn is not None:
            self.mysql_conn.close()
            self.mysql_conn = None
