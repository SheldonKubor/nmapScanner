import tkinter as tk
from  tkinter import ttk
from functools import partial

import socket
import sys
import time

import email.mime.text
import email.mime.multipart
import smtplib

import readPortBug as rb
import readPortService as rs
'''-----全局变量-----'''
bugMap = rb.bugMap()
serviceMap = rs.serviceMap()
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
s.connect((host, port))
mail_content = ''
'''-------------------------------------------'''
def send_url_to_server(scanIp,port):
    global mail_content
    global bugMap
    global serviceMap
    scanIpAndPort = scanIp
    print(scanIpAndPort)
    ipAndPort = ''
    ipAndPort = scanIpAndPort+','+str(port)
    print (ipAndPort)
    s.send(ipAndPort.encode('utf-8'))#
        # 接收小于 1024 字节的数据
    data = s.recv(1024)
    result = data.decode('utf-8')
    
    resultList = result.split(',')
    bugType = bugMap.get(resultList[0],'-')
    serviceType = serviceMap.get(resultList[0],'-')

    mail_content += result+','+serviceType+','+bugType+'\n'

    tree.insert("","end" ,values=(resultList[0],resultList[1],serviceType,bugType))
    #s.close()

    print (result)
    time.sleep(1)
    #s.close()

#send_url_to_server('123456789')
def sendUrl():
    urlAddress = urlEntry.get()
    beginPort = int(beginPortEntry.get())
    endPort = int(endPortEntry.get())
    for i in range(beginPort,endPort):
        send_url_to_server(urlAddress,i)

'''------------------------------------------'''
def delContent(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)

'''-------------------------------------------'''

def send_email(toAddress,content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'long time no see'
    msg['From'] = 'mjh123877@163.com'
    msg['To'] = toAddress

    print('+++++'+toAddress+'-----------')

    content = content
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 输入Email地址和口令:
    from_addr = 'mjh123877@163.com'
    #password = input('Password: ')
    # 输入收件人地址:
    to_addr = [toAddress]
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'


    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login('mjh123877@163.com', 'mjh1042800764') # 此处密码是客户端授权密码，不是邮箱原密码
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def sendEmail():
    emailAddress = emailEntry.get()
    send_email(emailAddress,mail_content)

def writeTxt():
    with open("扫描结果.txt","w+") as f:
        f.write(mail_content)
'''-------------------------------------------'''
root = tk.Tk()

root.title('nmap')
root.geometry('800x600')
    #urlFrame
topFrame = tk.Frame(root)
    #构造url那一行所需要的组件，一个label标签，一个输入框，两个按钮
urlLabel = tk.Label(topFrame,text="url")
urlEntry = tk.Entry(topFrame)

beginPortLabel = tk.Label(topFrame,text='开始端口')
beginPortEntry = tk.Entry(topFrame,width = 5)

endPortLabel = tk.Label(topFrame,text='结束端口')
endPortEntry = tk.Entry(topFrame,width = 5)
'''
#urlAddress = urlEntry.get()#获取输入框中的地址
#scanUrl = partial(ns.portScan,urlAddress,[8080,80])#增加参数，将url和端口号作为参数传递给send_mail函数
#sendUrl = partial(nc.send_url_to_server,urlAddress) #增加参数，将url发送给服务器
#scanButton = tk.Button(topFrame,text="扫描",command=scanUrl)
'''

scanButton = tk.Button(topFrame,text = '扫描',command = sendUrl)
    
reportButton = tk.Button(topFrame,text = "生成报告",command = writeTxt)
    #添加到父级容器中
urlLabel.pack(side = tk.LEFT)
urlEntry.pack(side = tk.LEFT)
beginPortLabel.pack(side = tk.LEFT)
beginPortEntry.pack(side = tk.LEFT)
endPortLabel.pack(side = tk.LEFT)
endPortEntry.pack(side = tk.LEFT)
scanButton.pack(side = tk.LEFT)
reportButton.pack(side = tk.LEFT)

    #emailFrame
midFrame = tk.Frame(root)
    #一个标签，一个输入框
emailLabel = tk.Label(midFrame,text='邮箱地址')
emailEntry = tk.Entry(midFrame)
'''
#emailAddress = emailEntry.get()  #获取输入框中的地址
#sendEmail = partial(ne.send_email,emailAddress) #增加参数，将地址作为参数传递给send_mail函数
'''
#发送邮件按钮
emailButton = tk.Button(midFrame,text = "发送邮件",command = sendEmail) # 获取email输入框的邮件地址
#添加到父级容器中
emailLabel.pack(side = tk.LEFT)
emailEntry.pack(side = tk.LEFT)
emailButton.pack(side = tk.RIGHT)
#resultFrame
bottomFrame = tk.Frame(root)
#一个表格
tree = ttk.Treeview(bottomFrame,show="headings", height=18, columns=("端口","开启状态","服务类型","危险的端口漏洞"))#生成一个表格
tree.column("端口",width=100,anchor="center")   #表示列,不显示  
tree.column("开启状态",width=100,anchor="center")  
tree.column("服务类型",width=100,anchor="center")
tree.column("危险的端口漏洞",width=100,anchor="center")

tree.heading("端口",text="端口")  #显示表头  
tree.heading("开启状态",text="开启状态")  
tree.heading("服务类型",text="服务类型") 
tree.heading("危险的端口漏洞",text="危险的端口漏洞") 
#添加到父级容器
tree.pack()
#将三个frame添加到根容器
topFrame.pack(side = tk.TOP)
midFrame.pack(side = tk.TOP)
bottomFrame.pack(side = tk.TOP)

root.mainloop()


