"""
socket client客户端编程
"""
import socket

class SocketClient:
    def __init__(self):
        # 创建socket对象
        self.__clientSocket = socket.socket(socket.AF_INET)

    def connect_server(self,host='localhost', port=8081):
        # 连接到server
        self.__clientSocket.connect((host, port))

    def recv_server(self):
        recv = self.__clientSocket.recv(1024);
        data = recv.decode(encoding="utf-8")
        return data
    def send(self,msg):
        data = msg.encode("utf-8")
        self.__clientSocket.send(data)

    def close(self):
        if self.__clientSocket != None:
            self.__clientSocket.close()


if __name__ == '__main__':

    client = SocketClient()
    client.connect_server()
    while True:
        in_  = input("客户端输入：")
        if in_ == "exit" :
            break
        #发送信息
        client.send(in_)
        #接收信息  阻塞  接收1024字节
        data = client.recv_server();
        print(f"客户端接收:{data}")

    client.close()