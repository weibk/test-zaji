#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/18 20:09


# 第三方SMTP服务器地址:
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.qq.com'
# 输入Email地址和授权码:
from_addr = 'w.yuling@qq.com'
password = 'kzbyqdwjhetvbggf'
# 输入收件人地址:
to_addr = 'weijiajian@wei.tax'

# 创建一个带附件的实例
message = MIMEMultipart('related')
# 定义发送人名字
message['From'] = Header('weibk', 'utf-8')
# 定义接收人的名字
message['To'] = Header('Jason', 'utf-8')
# 定义邮件主题
subject = '测试报告'
message['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="https://weibk.github.io">我的主页</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
fp = open('img.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

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
