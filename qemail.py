# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__user = "284159796@qq.com"
__pwd  = "qqyazsoicjmibjaf"
__to   = "284159796@qq.com"
# smutiorvysgofegf
def send_email(subject, body):
    if isinstance(body,unicode):
        body = str(body)

    if not isinstance(subject,unicode):
        subject = unicode(subject)

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = __user
    msg['To'] = __to
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="utf-8"
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(__user, __pwd)
        s.sendmail(__user, __to, msg.as_string())
        s.close()
        print 'send email ok'
        return True
    except Exception as e:
        print str(e)
        return False


# send_email('投x标信息', '投标信息\n投标信息\n投标信息\n投标信息\n')