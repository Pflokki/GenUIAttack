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
        while self.__running:
            data = self.connection.recv(2048)
            print(data)

    def set_status(self, int_code):
        if int_code in STATUS.items():
            self.status = int_code

    def set_address(self, address):
        self.address = address

    def stop(self):
        self.__running = False
        self.status = STATUS['offline']
        self.connection.close()
