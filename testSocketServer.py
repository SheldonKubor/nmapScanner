import socket
import sys

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
    try: 
        while True:
            ipAddress=clientsocket.recv(1024)
            print(ipAddress)

            t='qwerty'
            #print(t)
            clientsocket.send(t.encode('utf-8'))
    except socket.error:
        print('exit')
        #clientsocket.close()