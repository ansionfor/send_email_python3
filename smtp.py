#!/usr/local/bin/python3
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#收件人邮箱
to_addr = '****@qq.com'

# 第三方 SMTP 服务

smtp_server="smtp.qq.com"  #设置服务器
mail_user="****@qq.com"    #发件人邮箱
mail_pass="********"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % mail_user)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(mail_user, mail_pass)
server.sendmail(mail_user, [to_addr], msg.as_string())
server.quit()
