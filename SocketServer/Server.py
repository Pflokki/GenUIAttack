from threading import Thread
import socket

from SocketServer.NodePool import ClientNodePool
from SocketServer.Node import ClientNode


TCP_IP = '127.0.0.1'
TCP_PORT = 8080


class Server(Thread):
    def __init__(self, window):
        super().__init__()
        self.client_pool = ClientNodePool()
        self.window = window

    def run(self) -> None:
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind((TCP_IP, TCP_PORT))

        tcp_server.listen(5)
        print("Start listening")
        while True:
            (connection, (ip, port)) = tcp_server.accept()
            print("New Connection from {}:{}".format(ip, port))
            client_node = ClientNode(connection)
            client_node.set_address((ip, port))
            self.client_pool.add(client_node)
            self.window.update_connection(self.client_pool)
            client_node.start()
