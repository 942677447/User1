import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QApplication,QWidget,QLineEdit,
    QPushButton,QLabel,QHBoxLayout,
    QVBoxLayout
)

class Menu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lounge Cafe")
        self.setFixedSize(320,200)
        self.initUI()
        self.show()
    
    def initUI(self):
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.btn_food = QPushButton("Fast Food")
        self.btn_Ice = QPushButton("Ice cream")
        self.btn_drinks = QPushButton("Drinks")

        self.h_box1.addWidget(self.btn_food)
        self.h_box2.addWidget(self.btn_Ice)
        self.h_box3.addWidget(self.btn_drinks)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)

        self.setLayout(self.v_box)

class Fast_Food(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Fast food")
        self.setFixedSize(320,200)
        self.initUI()
        self.show()
    
    def initUI(self):
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()
        self.h_box7 = QHBoxLayout()

app = QApplication([])
win = Menu()
sys.exit(app.exec_())

