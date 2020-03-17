from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class InfoWindowControl(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui/design.ui", self)

        self.setWindowTitle("Информация о жертве")
        self.init_plot()

        self.cpu = []
        self.ram = []
        self.connect = []
        self.traffic = []

    def set_info(self, cpu, ram, connect, traffic):
        self.cpu = cpu
        self.ram = ram
        self.connect = connect
        self.traffic = traffic

        self.plotting_pictures()

    def init_plot(self):
        self.MplWidget_CPU.canvas.axes.set_title('Нагрузка ЦП, %')
        self.MplWidget_CPU.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_CPU.canvas.axes.set_ylabel("Процент загрузки, %")
        self.MplWidget_CPU.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_RAM.canvas.axes.set_title('Нагрузка ОЗУ, %')
        self.MplWidget_RAM.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_RAM.canvas.axes.set_ylabel("Процент загрузки, %")
        self.MplWidget_RAM.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_Connects.canvas.axes.set_title('Установленные соединения, %')
        self.MplWidget_Connects.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_Connects.canvas.axes.set_ylabel("Процент соединений, %")
        self.MplWidget_Connects.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_Traffic.canvas.axes.set_title('Суммарный объем сетевого трафика, пак/с')
        self.MplWidget_Traffic.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_Traffic.canvas.axes.set_ylabel("Количество пакетов")

    def plotting_pictures(self):
        self.MplWidget_CPU.canvas.axes.clear()
        self.MplWidget_RAM.canvas.axes.clear()
        self.MplWidget_Connects.canvas.axes.clear()
        self.MplWidget_Traffic.canvas.axes.clear()

        self.init_plot()

        self.MplWidget_CPU.canvas.axes.plot(self.cpu)
        self.MplWidget_RAM.canvas.axes.plot(self.ram)
        self.MplWidget_Connects.canvas.axes.plot(self.connect)
        self.MplWidget_Traffic.canvas.axes.plot(self.traffic)

        self.MplWidget_CPU.canvas.draw()
        self.MplWidget_RAM.canvas.draw()
        self.MplWidget_Connects.canvas.draw()
        self.MplWidget_Traffic.canvas.draw()
