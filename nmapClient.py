import tkinter as tk
import nmapEmail as ne
from  tkinter import ttk
def nmapClientUi():
    root = tk.Tk()

    root.title('nmap')
    root.geometry('800x600')

    topFrame = tk.Frame(root)

    urlLabel = tk.Label(topFrame,text="url")
    urlEntry = tk.Entry(topFrame)
    scanButton = tk.Button(topFrame,text="扫描")
    reportButton = tk.Button(topFrame,text = "生成报告")

    urlLabel.pack(side = tk.LEFT)
    urlEntry.pack(side = tk.LEFT)
    scanButton.pack(side = tk.LEFT)
    reportButton.pack(side = tk.LEFT)

    midFrame = tk.Frame(root)

    emailLabel = tk.Label(midFrame,text='邮箱地址')
    emailEntry = tk.Entry(midFrame)
    emailButton = tk.Button(midFrame,text = "发送邮件",command=ne.send_email)

    emailLabel.pack(side = tk.LEFT)
    emailEntry.pack(side = tk.LEFT)
    emailButton.pack(side = tk.RIGHT)

    bottomFrame = tk.Frame(root)
    tree = ttk.Treeview(bottomFrame,show="headings", height=18, columns=("端口","开启状态","服务类型","危险的端口漏洞"))
    tree.column("端口",width=100,anchor="center")   #表示列,不显示  
    tree.column("开启状态",width=100,anchor="center")  
    tree.column("服务类型",width=100,anchor="center")
    tree.column("危险的端口漏洞",width=100,anchor="center")

    tree.heading("端口",text="端口")  #显示表头  
    tree.heading("开启状态",text="开启状态")  
    tree.heading("服务类型",text="服务类型") 
    tree.heading("危险的端口漏洞",text="危险的端口漏洞") 

    tree.pack()

    topFrame.pack(side = tk.TOP)
    midFrame.pack(side = tk.TOP)
    bottomFrame.pack(side = tk.TOP)

    root.mainloop()
if __name__ == '__main__':
    nmapClientUi()