import requests

hitokoto=requests.get("https://v1.hitokoto.cn?c=i").json()["hitokoto"]
author=requests.get("https://v1.hitokoto.cn?c=i").json()["from_who"]
title=requests.get("https://v1.hitokoto.cn?c=i").json()["from"]



def sent_email(subject, message):
    
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    from email.utils import formataddr

    mail_host = "smtp.163.com"
    mail_user = "mojinxin0001@163.com"
    mail_pass = "CFTdQ6gz2uusca3q"  # 授权码

    sender = mail_user
    receivers = ['mojinxin2022@163.com']

    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = formataddr((Header("每日一言", 'utf-8').encode(), sender))
    message['To'] = formataddr((Header('', 'utf-8').encode(), receivers[0]))
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)

sent_email(hitokoto,f'来自{title}的{author}')
