import socket
import sys
import time

def send_url_to_server(scanIp):
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # 获取本地主机名
    host = socket.gethostname() 

    # 设置端口好
    port = 9999
    scanIpAndPort = scanIp
    print(scanIpAndPort)
    # 连接服务，指定主机和端口
    s.connect((host, port))
    for i in range(10):
        ipAndPort = ''
        ipAndPort = scanIpAndPort+','+str(i)
        print (ipAndPort)
        s.send(ipAndPort.encode('utf-8'))#
        # 接收小于 1024 字节的数据
        data = s.recv(1024)

        #s.close()

        print (data.decode('utf-8'))
        time.sleep(1)

#send_url_to_server('123456789')
