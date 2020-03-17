from threading import Thread
from Messages import StartAttackMessage, StopAttackMessage

STATUS = ['offline', 'online', 'attacked', 'down']


class ClientNode(Thread):
    def __init__(self, connection):
        super().__init__()

        self.address = None
        self.status = STATUS[0]

        self.__running = True
        self.connection = connection

    def run(self) -> None:
        self.status = STATUS[1]
        while self.__running:
            data = self.connection.recv(2048).decode("UTF8")
            if len(data) and data[-1] == '\n':
                self.on_msg_event(data[:-1])

    def on_msg_event(self, data):
        print("i: {}".format(data))

    def set_status(self, int_code):
        if 0 <= int_code <= len(STATUS):
            self.status = STATUS[int_code]

    def set_address(self, address):
        self.address = address

    def stop(self):
        self.__running = False
        self.status = STATUS[0]
        self.connection.close()

    def start_attack(self):
        self.send_message(StartAttackMessage().get_message())
        self.status = STATUS[2]

    def stop_attack(self):
        self.send_message(StopAttackMessage().get_message())
        self.status = STATUS[1]

    def send_message(self, message):
        print("o: {}".format(message))
        self.connection.send(message)
