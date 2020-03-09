
class ClientNodePool:
    def __init__(self):
        self.__iter_value = 0
        self.client_nodes = []

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.__iter_value += 1
    #     if not len(self._client_nodes) \
    #             or self.__iter_value > len(self._client_nodes):
    #         raise StopIteration
    #     else:
    #         return self._client_nodes[self.__iter_value - 1]

    def add(self, client_node):
        self.client_nodes.append(client_node)

    def close_connections(self):
        for node in self.client_nodes:
            node.stop()
        self.client_nodes.clear()

    def start_attack(self):
        for node in self.client_nodes:
            node.start_attack()

    def stop_attack(self):
        for node in self.client_nodes:
            node.stop_attack()
