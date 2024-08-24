# - *- coding: utf-8 -* -
from python_mcstatus import JavaStatusResponse, statusJava
from MCSContent import *

host = 'play.simpfun.cn'
start_port = int(input("请输入开始端口:"))
end_port = int(input("请输入结束端口:"))
query = True
for i in range(start_port,end_port):
    status = statusJava(host, i, query)
    if status.online:
        version=vscontent(status)
        motd=mdcontent(status)
        result="host:"+status.host+" "+"port:"+str(status.port)+" "+"version:"+version+" "+"motd:"+motd
        with open ('result.txt','a') as file:
            file.writelines(result+"\n")
            file.close()
            print(status.host+":"+str(status.port)+"online")
    else:
        print(status.host+":"+str(status.port)+"offline")

print("查询结果在result.txt")
