def bugMap():
    bugMap = {}
    with open('端口漏洞.txt','r') as f:
        textList = f.readlines()
        for line in textList:
            lineList = line.strip().split(',')
            #print(lineList[0]+lineList[1])
            bugMap[lineList[0]] = lineList[1]
    print(bugMap)
    return bugMap
#bugMap()
        