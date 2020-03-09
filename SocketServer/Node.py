from threading import Thread


STATUS = {
    'offline': -1,
    'online': 0,
    'attacked': 1,
    'down': 2
}


class ClientNode(Thread):
    def __init__(self, connection):
        super().__init__()

        self.address = None
        self.status = STATUS['offline']

        self.__running = True
        self.connection = connection

    def run(self) -> None:
        self.status = STATUS['online']
        while self.__running:
            data = self.connection.recv(2048).decode("UTF8")
            if len(data) and data[-1] == '\n':
                self.on_msg_event(data[:-1])

    def on_msg_event(self, data):
        print("i: {}".format(data))

    def set_status(self, int_code):
        if int_code in STATUS.items():
            self.status = int_code

    def set_address(self, address):
        self.address = address

    def stop(self):
        self.__running = False
        self.status = STATUS['offline']
        self.connection.close()

    def start_attack(self):
        self.send_message("Start attack")
        self.status = STATUS['attacked']

    def stop_attack(self):
        self.send_message("Stop attack")
        self.status = STATUS['online']

    def send_message(self, message):
        print("o: {}".format(message))
        self.connection.send("{}\n".format(message).encode())
