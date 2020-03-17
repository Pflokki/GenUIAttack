
class ClientNodePool:
    def __init__(self):
        self.__iter_value = 0
        self.client_nodes = []

    def add(self, client_node):
        self.client_nodes.append(client_node)

    def close_connections(self):
        for node in self.client_nodes:
            node.stop()
        self.client_nodes.clear()

    def start_attack(self):
        for node in self.client_nodes:
            try:
                node.start_attack()
            except (BrokenPipeError, OSError):
                node.stop()

    def stop_attack(self):
        for node in self.client_nodes:
            try:
                node.stop_attack()
            except (BrokenPipeError, OSError):
                node.stop()
