#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/12 10:22

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入Email地址和授权码:
from_addr = 'w.yuling@qq.com'
password = 'kzbyqdwjhetvbggf'
# 输入收件人地址:
to_addr = 'weijiajian@wei.tax'

# 创建一个带附件的实例
message = MIMEMultipart()
# 定义发送人名字
message['From'] = Header('Python', 'utf-8')
# 定义接收人的名字
message['To'] = Header('测试员', 'utf-8')
# 定义邮件主题
subject = 'Python SMTP 带附件的邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文：
message.attach(MIMEText('这封邮件带了两个附件.....', 'plain', 'utf-8'))

# 添加第一个附件，传送当前目录下的 abs_test.py 文件
att1 = MIMEText(open('abs_test.py').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="abs_test.py"'
message.attach(att1)

# 添加第二个附件
att2 = MIMEText(open('calc_test.py').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att2["Content-Disposition"] = 'attachment; filename="calc.py"'
message.attach(att2)
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
