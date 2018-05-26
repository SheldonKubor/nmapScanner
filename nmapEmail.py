import email.mime.text
import email.mime.multipart
import smtplib
def send_email(toAddress):
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'long time no see'
    msg['From'] = 'mjh123877@163.com'
    msg['To'] = toAddress
    content = '''
        dear friend
            how about have dinner together tonight?
            please call me back.
            yours constantine
    '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 输入Email地址和口令:
    from_addr = 'mjh123877@163.com'
    #password = input('Password: ')
    # 输入收件人地址:
    to_addr = '1042800764@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'


    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login('mjh123877@163.com', 'mjh1042800764') # 此处密码是客户端授权密码，不是邮箱原密码
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()