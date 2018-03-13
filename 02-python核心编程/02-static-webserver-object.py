# -*- coding:utf-8 -*-


from socket import * 
from multiprocessing import Process

import re


# 资源家目录
BASE_DIR = "./http"


class HTTPServer(object):
    """"""

    def __init__(self, port):
        # 创建tcp_socket
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        # 处理端口重复
        self.tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定ip和端口
        self.tcp_socket.bind(("", port))
        # 设定监听
        # tcp_socket.listen(5)
        
    def run(self):
        """"""
        # 设定监听
        self.tcp_socket.listen(5)
        while True:

            # 处理接收,这里的进程会堵塞
            client_socket_info = self.tcp_socket.accept()
            # 添加多进程
            client_pro = Process(target=self.handle_client, args=(client_socket_info, ))
            client_pro.start()
            # 因为python进程有写时copy
            client_socket_info[0].close()
        
    def handle_client(self, client_socket_info):
        """"""
        # 接收信息
        client_socket, client_info = client_socket_info
        msg = client_socket.recv(1024)
        
        # 处理http请求
        # 将msg转成utf-8
        msg = msg.decode("utf-8")        
        # 处理第一行数据
        http_head = msg.splitlines()[0]
        http_head_group = re.match("(\w+) (.+) ", http_head)
        http_method = http_head_group.group(1)
        http_url = http_head_group.group(2)
        print(http_url)
        # 处理静态资源
        if http_url == "/":
            http_url = "/index.html"
        try:
            # 打开本地资源家目录
            open_file_path = BASE_DIR+http_url
            http_source = open(open_file_path, "br")
            http_source_content = http_source.read()        
        except IOError:
            # 资源不存在
            # 返回http响应
            response_head_status = "404 Not Found"
            http_source_content = " not found ".encode("utf-8")
        else:
            http_source.close()
            # 返回http响应
            response_head_status = "200 OK"
            
        response_head_p = "HTTP/1.1 "
        response_head_server = "gserver: 0.0.1"
        response_head = response_head_p + response_head_status +"\r\n"+response_head_server+"\r\n\r\n"

        print("-------------------------------------")
        response_head = response_head.encode("utf-8")

        response = response_head + http_source_content
        
        print(response)
        # 发送响应
        client_socket.send(response)
        print("--------------------------------退出...")
        client_socket.close()
                   

if __name__ == "__main__":
    
    # 创建对象
    http_server = HTTPServer(8080)
    # 开启
    http_server.run()



