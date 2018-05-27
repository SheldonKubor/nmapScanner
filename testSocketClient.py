import socket
import sys
import time


# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # 获取本地主机名
host = socket.gethostname() 

    # 设置端口好
port = 9999
scanIpAndPort = '1234567'
#print(scanIpAndPort)
    # 连接服务，指定主机和端口
s.connect((host, port))

for i in range(10):
    s.send(scanIpAndPort.encode('utf-8'))
    # 接收小于 1024 字节的数据
    data = s.recv(1024)
    print (data.decode('utf-8'))
    print (scanIpAndPort)
    time.sleep(1)
    #s.close()

#print (data.decode('utf-8'))