"""
socket server 服务端编程
"""
import socket
class SocketServer:
    def __init__(self,host = "localhost",port = 8081,listensize = 10):
        self.bind(host, port, listensize)

    def bind(self,host:str,port:int,listensize :int):
        # 创建socket对象
        self.__serverSocket = socket.socket(socket.AF_INET)
        # 绑定ip 端口
        self.__serverSocket.bind((host, port))
        # 监听端口  允许连接的数量    设置1就是允许连接一个
        self.__serverSocket.listen(listensize)

    def connect_client(self):
        # 等待客户端连接
        #wait_client_result :tuple = self.__serverSocket.accept()
        # conn = wait_client_result[0]
        # address = wait_client_result[1]
        self.__conn, addr = self.__serverSocket.accept()

    def recv_client(self):
        """
        接收客户端信息
        :return:
        """
        recv = self.__conn.recv(1024);
        data = recv.decode("utf-8")
        return data

    def send(self,msg :str):
        """
        发送信息
        :param msg:
        :return:
        """
        data = msg.encode("utf-8")
        self.__conn.send(data)

    def close(self):
        """
        连接关闭
        """
        if self.__serverSocket != None:
            if self.__conn != None:
                self.__conn.close()
            self.__serverSocket.close()



if __name__ == "__main__":

    server = SocketServer()
    server.connect_client()

    while True:
        data = server.recv_client()
        print(f"服务端接收:{data}")

        in_ = input("服务端输入：")
        if in_ == "exit" :
            break

        server.send(in_)

    server.close()
