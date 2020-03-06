from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.uic import loadUi


class MainWindowControl(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui/mainwindow.ui", self)
        self.init_table_widget()

    def init_table_widget(self):
        self.tW_NodeStatus.setRowCount(0)
        self.tW_NodeStatus.setColumnCount(2)

        header = self.tW_NodeStatus.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        for index, name in enumerate(["Адрес узла", "Состояние"]):
            self.tW_NodeStatus.setHorizontalHeaderItem(index, QTableWidgetItem(name))
        self.tW_NodeStatus.insertRow(0)

    def update_connection(self, node_pool):
        self.init_table_widget()
        for row_count, node in enumerate(node_pool.client_nodes):
            self.tW_NodeStatus.insertRow(row_count)
            self.tW_NodeStatus.setItem(row_count, 0, QTableWidgetItem(str(node.address)))
            self.tW_NodeStatus.setItem(row_count, 1, QTableWidgetItem(str(node.status)))
