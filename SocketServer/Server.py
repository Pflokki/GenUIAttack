from threading import Thread
import socket

from SocketServer.NodePool import ClientNodePool
from SocketServer.Node import ClientNode, STATUS


TCP_IP = '127.0.0.1'
TCP_PORT = 8080


class Server(Thread):
    def __init__(self, window):
        super().__init__()
        self.client_pool = ClientNodePool()
        self.window = window
        self._stop_flag = True

    def run(self) -> None:
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind((TCP_IP, TCP_PORT))

        tcp_server.listen(5)
        print("Start listening")
        while self._stop_flag:
            (connection, (ip, port)) = tcp_server.accept()
            print("New Connection from {}:{}".format(ip, port))
            client_node = ClientNode(connection)
            client_node.set_address((ip, port))
            client_node.set_status(0)
            self.client_pool.add(client_node)
            client_node.start()
            self.window.set_btn_callback(self.start_attack, self.stop_attack)
            self.window.update_connection(self.client_pool)

    def start_attack(self):
        print("[Server] Start attack")

    def stop_attack(self):
        print("[Server] Stop attack")

    def stop_server(self):
        print("Server stopped")
        self._stop_flag = False
        self.client_pool.close_connections()
