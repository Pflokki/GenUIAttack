from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.uic import loadUi


class MainWindowControl(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui/mainwindow.ui", self)
        self.init_table_widget()

        self.attack_btn_callback = None
        self.stop_attack_btn_callback = None
        self.client_status_callback = None

        self.pB_StartAttack.clicked.connect(self.on_click_attack_btn)
        self.pB_StopAttack.clicked.connect(self.on_click_stop_attack_btn)

        self.tW_NodeStatus.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tW_NodeStatus.itemClicked.connect(self.on_click_client_row)

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

    def on_click_attack_btn(self):
        print("[Window] Start attack")
        if self.attack_btn_callback is not None:
            self.attack_btn_callback()

    def on_click_stop_attack_btn(self):
        print("[Window] Stop attack")
        if self.stop_attack_btn_callback is not None:
            self.stop_attack_btn_callback()

    def on_click_client_row(self):
        client_row = self.tW_NodeStatus.selectionModel().selectedRows()[0]
        self.client_status_callback(client_row.row())

    def set_btn_callback(self, attack_btn_callback, stop_attack_btn_callback, client_status_callback):
        self.attack_btn_callback = attack_btn_callback
        self.stop_attack_btn_callback = stop_attack_btn_callback
        self.client_status_callback = client_status_callback
