# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:08:41 2019

@author: DJ萧
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('test')   # 邮件内容
message['From'] = Header('小艾')   # 邮件发送者名字
message['To'] = Header('mas')   # 邮件接收者名字
message['Subject'] = Header('常规报告')   # 邮件主题

mail = smtplib.SMTP()
mail.connect("smtp.qq.com")   # 连接 qq 邮箱
mail.login("892065502@qq.com", "lhvgtxxsrtnlbcjg")   # 账号和授权码
mail.sendmail("892065502@qq.com", ["892065502@qq.com"], message.as_string())   # 发送账号、接收账号和邮件信息

#from_addr ="892065502@qq.com"
#password = "lhvgtxxsrtnlbcjg"



