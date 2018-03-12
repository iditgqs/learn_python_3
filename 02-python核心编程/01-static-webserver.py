# -*- coding:utf-8 -*-


from socket import * 
from multiprocessing import Process

import re


# 资源家目录
BASE_DIR = "./http"

# 创建tcp_socket
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 处理端口重复
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定ip和端口
tcp_socket.bind(("", 8080))
# 设定监听
tcp_socket.listen(5)


# 处理client
def handle_client(client_socket_info):
#  while True:

    # 接收信息
    client_socket, client_info = client_socket_info
    msg = client_socket.recv(1024)
    
    print(msg)
    # 处理http请求
    # 将msg转成utf-8
    msg = msg.decode("utf-8")        
    # 处理第一行数据
    http_head = msg.splitlines()[0]
    http_head_group = re.match("(\w+) (.+) ", http_head)
    http_method = http_head_group.group(1)
    http_url = http_head_group.group(2)
    # 处理静态资源
    if http_url == "/":
        http_url = "/index.html"
    # 打开本地资源家目录
    open_file_path = BASE_DIR+http_url
    http_source = open(open_file_path, "br")
    http_source_content = http_source.read()        
    http_source.close()
    
    # 返回http响应
    response_head_p = "HTTP/1.1 "
    response_head_status = "200 OK"
    response_head_server = "gserver: 0.0.1"

    response_head = response_head_p + response_head_status +"\r\n"+response_head_server+"\r\n\r\n"        
    response = response_head.encode("utf-8") + http_source_content
    
    print(response)
    # 发送响应
    client_socket.send(response)
    print("--------------------------------退出...")
    client_socket.close()
               

#  if len(msg) == 0:
#      print("%s 已退出..."%str(client_info))
#      client_socket.close()
#      break

# print("%s: %s"%(client_info,msg))


while True:

    # 处理接收,这里的进程会堵塞
    client_socket_info = tcp_socket.accept()
    # 添加多进程
    client_pro = Process(target=handle_client, args=(client_socket_info, ))
    client_pro.start()
    # 因为python进程有写时copy
    client_socket.close()

