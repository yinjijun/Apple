# -*- coding: utf-8 -*-
# @project  : Apple
# @author   : yinjijun
# @file     : db.py
# @ide      : PyCharm
# @time     : 2020/8/13 11:50
import pymysql
from time import sleep
DB = pymysql.connect(
                       host='192.168.2.187',
                       port=3306,
                       user='yinjijun',
                       password='1234pl',
                       db='cnj_uall',
                       charset='utf8')
cursor = DB.cursor()
while True:
    tele = input('手机号码：')
    sleep(2)
    if len(tele) == 11 and tele.isdigit():
        tel = int(tele)
        cursor.execute(f'SELECT * FROM (SELECT `code` FROM modoer_members_sendmobile WHERE mobile={tel} ORDER BY id DESC) as f LIMIT 1')
        ret = cursor.fetchall()
        res = ret[0][0]
        print('验证码：',res)
    else:
        print('手机号错误，请重新输入')