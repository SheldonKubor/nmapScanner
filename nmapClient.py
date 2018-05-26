import tkinter as tk
from  tkinter import ttk
from functools import partial

import nmapEmail as ne
import nmapScan as ns
import socketClient as nc

def sendEmail():
    emailAddress = emailEntry.get()
    ne.send_email(emailAddress)
def sendUrl():
    urlAddress = urlEntry.get()
    nc.send_url_to_server(urlAddress)

root = tk.Tk()

root.title('nmap')
root.geometry('800x600')
    #urlFrame
topFrame = tk.Frame(root)
    #构造url那一行所需要的组件，一个label标签，一个输入框，两个按钮
urlLabel = tk.Label(topFrame,text="url")
urlEntry = tk.Entry(topFrame)

'''
#urlAddress = urlEntry.get()#获取输入框中的地址
#scanUrl = partial(ns.portScan,urlAddress,[8080,80])#增加参数，将url和端口号作为参数传递给send_mail函数
#sendUrl = partial(nc.send_url_to_server,urlAddress) #增加参数，将url发送给服务器
#scanButton = tk.Button(topFrame,text="扫描",command=scanUrl)
'''

scanButton = tk.Button(topFrame,text = '扫描',command = sendUrl)
    
reportButton = tk.Button(topFrame,text = "生成报告")
    #添加到父级容器中
urlLabel.pack(side = tk.LEFT)
urlEntry.pack(side = tk.LEFT)
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
emailButton = tk.Button(midFrame,text = "发送邮件",command=sendEmail) # 获取email输入框的邮件地址
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


