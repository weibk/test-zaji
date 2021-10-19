#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/18 10:39

from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

print(HTMLTestRunner.HTMLTestRunner)
tests = unittest.defaultTestLoader.discover(
    r'H:\G\pythonProject\test-zaji\unit', pattern='calc_test.py')
runner1 = HTMLTestRunner.HTMLTestRunner(
    stream=open(file="calcreport.html", mode="w+", encoding='utf-8'),
    title='计算器测试',
    description='计算器测试报告',
    verbosity=1
)
runner1.run(tests)

# 第三方SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入Email地址和授权码:
from_addr = 'w.yuling@qq.com'
password = 'kzbyqdwjhetvbggf'
# 输入收件人地址:
to_addr = 'q2219625857@qq.com'

# 创建一个带附件的实例
message = MIMEMultipart()
# 定义发送人名字
message['From'] = Header('weibk', 'utf-8')
# 定义接收人的名字
message['To'] = Header('Jason', 'utf-8')
# 定义邮件主题
subject = '测试报告'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文：
message.attach(MIMEText('计算器测试报告', 'plain', 'utf-8'))

# 添加第一个附件，传送当前目录下的 abs_test.py 文件
att1 = MIMEText(open('calcreport.html', encoding='utf-8').read(), 'base64',
                'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="calcreport.html"'
message.attach(att1)

# 尝试发送邮件
try:
    # 创建SMTP对象
    smtpObj = smtplib.SMTP()
    # 创建SMTP连接
    smtpObj.connect(smtp_server, 25)  # SMTP的端口号，一般为25
    # 登录邮箱
    smtpObj.login(from_addr, password)
    # 发送邮件 发送方  接收方  信息
    smtpObj.sendmail(from_addr, to_addr, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:邮件发送失败')
