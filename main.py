from PyQt5.QtWidgets import QApplication
from uiControl.MainWindowControl import MainWindowControl

from SocketServer.Server import Server


def main():
    app = QApplication([])
    window = MainWindowControl()
    tcp_server = Server(window)
    tcp_server.start()
    window.show()
    app.exec_()
    tcp_server.stop_server()


if __name__ == '__main__':
    main()
