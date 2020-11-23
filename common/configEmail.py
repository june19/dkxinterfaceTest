#主要是配置发送邮件的主题，正文等，将测试报告发送并抄送到相关邮件逻辑

import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail(object):
    def __init__(self,username,passwd,recv,title,content,file=None,ssl=False,email_host='smtp.163.com',port=25,ssl_port=465):
        self.username = username #用户名
        self.passwd = passwd #密码
        self.recv = recv
        self.title = title   #邮件标题
        self.content = content  #邮件正文
        self.file = file   #附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host   #smtp服务器地址
        self.port = port   #普通端口
        self.ssl = ssl        #是否安全连接
        self.ssl_port = ssl_port   #安全连接端口

    def send_email(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:   #处理附件的
            file_name = os.path.split(self.file)[-1] #只取文件名，不取路径
            try:
                f = open(self.file,'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！')
            else:
                att = MIMEText(f,"base64","utf-8")
                att["Content-Type"]='application/octet-stream'
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                #这里是处理温江名为中文名的，必须这么写
                att["Content-Disposition"]='attachment; filename="%s"'%(new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content)) #邮件正文的内容
        msg['subject'] = self.title #邮件主题
        msg['From'] = self.username #发送者账号
        msg['TO'] =','.join(self.recv) #接受者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp =smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print("出错了...",e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m=SendEmail(
        username ='june_tangli@163.com',
        passwd='613088jun',
        recv= ['zhangke927@163.com','june_tangli@163.com'],
        title='test20201118',
        content='测试发送邮件',
        file=r'E:\pydj\test_record\test.png',
        ssl=True,

    )
    m.send_email()



