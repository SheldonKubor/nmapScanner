import socket
import sys
import nmapScan as ns


# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    
    ipAddress=clientsocket.recv(1024)
    print(ipAddress)

    ns.portScan(ipAddress,[80])#先写死端口

    clientsocket.send('receive'.encode('utf-8'))
        #clientsocket.close()