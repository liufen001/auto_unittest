# -*- coding: utf-8 -*-

'''
Created on 2017年7月16日

@author: Administrator
'''

from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class MailSender(object):
    "发送邮件类"

    def __init__(self, smtp_server, username, password):
        "登录SMTP服务器"
        self._username = username

        self.email_client = SMTP(smtp_server)
        self.email_client.login(username, password)

    def send(self, to_addr, subject, content, text_type='plain', attachment=None):
        "发送邮件"

        if attachment == None:
            msg = MIMEText(content, text_type, 'utf-8')
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = '<' + self._username + '>'
            msg['To'] = to_addr
        elif isinstance(attachment, str):
            msg = MIMEMultipart()
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = '<' + self._username + '>'
            msg['To'] = to_addr
            # 构造附件1，传输当前目录下的foo.txt文件
            att = MIMEText(open(attachment, "rb").read(), 'base64', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename=%s' % attachment
            msg.attach(MIMEText(content, text_type, 'utf-8'))
            msg.attach(att)

        elif isinstance(attachment, list):
            pass
        else:
            raise Exception("attachment参数非法")

        self.email_client.sendmail(self._username, to_addr, msg.as_string())
        return

    def quit(self):
        # 结束SMTP会话
        self.email_client.quit()

def send_test_report(report,subject,content,to_addrs):
    ms = MailSender("smtp.qq.com", "122815306@qq.com", "kehewnpaprmkbheh")
    if isinstance(to_addrs,list):
        for to_addrs in to_addrs:
            ms.send(to_addrs, subject, content, 'html',report)
    elif isinstance(to_addrs,str):
        ms.send(to_addrs, subject, content, 'html',report)
    else:
        raise Exception('收件人邮箱输入有误')
    ms.quit()


if __name__ == '__main__':
      ms = MailSender("smtp.qq.com", "122815306@qq.com", "kehewnpaprmkbheh")
      ms.send("1148270541@qq.com", "吃饭", "8点吃饭", "plain", "foo.txt")
#     #
#     # ms.quit()
#     #send_test_report('../Result/report/20180731_103409htmlreport.html','测试报告','请查收测试报告','1148270541@qq.com')
     #send_test_report('../Result/report/20180731_103409htmlreport.html','测试报告','请查收测试报告',['1337320943@qq.com','1148270541@qq.com','122815306@qq.com'])


