# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:08:41 2019

@author: DJ萧
"""
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

if time.localtime(time.time()).tm_wday in range(0,4):
    message = MIMEText('test')   # 邮件内容
    message['From'] = Header('小艾')   # 邮件发送者名字
    message['To'] = Header('mas')   # 邮件接收者名字
    message['Subject'] = Header('基金时间提醒')   # 邮件主题
    
    mail = smtplib.SMTP()
    mail.connect("smtp.qq.com")   # 连接 qq 邮箱
    mail.login("*******@qq.com", "*******")   # 账号和授权码
    mail.sendmail("*******@qq.com", ["*******@qq.com"], message.as_string())   # 发送账号、接收账号和邮件信息
    
    #from_addr ="******@qq.com"
    #password = "***********"



