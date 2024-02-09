from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
import sqlite3
from PyQt5 import uic
from random import randint
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setColumnWidth(0, 15)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 100)
        connect = sqlite3.connect('coffee.sqlite')
        curser = connect.cursor()
        res = curser.execute("""SELECT * FROM info""").fetchall()
        self.tableWidget.setRowCount(len(res))
        for i in range(len(res)):
            coffee = list(res[i])
            if coffee[3] == 0:
                coffee[3] = 'молотый'
            else:
                coffee[3] = 'в зернах'
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(coffee[j])))
        connect.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
