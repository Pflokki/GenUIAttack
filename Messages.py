import json


class Message:
    def __init__(self):
        self.msg = {'t': "Ping"}

    def get_message(self):
        return json.dumps(self.msg).encode()


class StartAttackMessage(Message):
    def __init__(self):
        super().__init__()
        self.msg = {'t': "StartAttack"}


class StopAttackMessage(Message):
    def __init__(self):
        super().__init__()
        self.msg = {'t': "StopAttack"}


class GetStatus(Message):
    def __init__(self):
        super().__init__()
        self.msg = {'t': "GetStatus"}
