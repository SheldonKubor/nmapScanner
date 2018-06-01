def serviceMap():
    serviceMap = {}
    with open('端口对应服务.txt','r') as f:
        textList = f.readlines()
        for line in textList:
            lineList = line.strip().split('=')
            serviceMap[lineList[0]] = lineList[1]
    print(serviceMap)
    return serviceMap
serviceMap()