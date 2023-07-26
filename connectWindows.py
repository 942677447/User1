import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel,
    QPushButton
)

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Main")
        self.setFixedSize(400,300)
        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label = QLabel('Main page')

        self.btn_next = QPushButton('next')
        self.btn_back = QPushButton('back')
        

        self.h_box.addStretch()
        self.h_box.addWidget(self.btn_back)
        self.h_box.addWidget(self.btn_next)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.btn_back.clicked.connect(self.on_back)
        self.btn_next.clicked.connect(self.on_next)

    def on_back(self):
        self.thi = ThirdWindow()
        self.close()

    def on_next(self):
        self.sec = SecondWindow()
        self.close()

class SecondWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setFixedSize(400,300)
        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label = QLabel('Second page')

        self.btn_main = QPushButton('main')
        self.btn_next = QPushButton('next')
        self.btn_back = QPushButton('back')

        self.h_box.addWidget(self.btn_main)
        self.h_box.addStretch()
        self.h_box.addWidget(self.btn_back)
        self.h_box.addWidget(self.btn_next)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.btn_main.clicked.connect(self.to_Main_Page)
        self.btn_back.clicked.connect(self.to_back)
        self.btn_next.clicked.connect(self.to_third)

    def to_Main_Page(self):
        self.main = MainWindow()
        self.close()

    def to_back(self):
        self.main = MainWindow()
        self.close()
        
    def to_third(self):
        self.next = ThirdWindow()
        self.close()

class ThirdWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Third Window")
        self.setFixedSize(400,300)
        self.initUI()
        self.show()

    def initUI(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label = QLabel('Third page')

        self.btn_main = QPushButton('main')
        self.btn_next = QPushButton('next')
        self.btn_back = QPushButton('back')

        self.h_box.addWidget(self.btn_main)
        self.h_box.addStretch()
        self.h_box.addWidget(self.btn_back)
        self.h_box.addWidget(self.btn_next)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.btn_back.clicked.connect(self.to_back)
        self.btn_main.clicked.connect(self.to_Main)
    
    def to_back(self):
        self.back = SecondWindow()
        self.close()
    
    def to_Main(self):
        self.main = MainWindow()
        self.close()


app = QApplication([])
win = MainWindow()
# sec = SecondWindow()
# thi = ThirdWindow()
sys.exit(app.exec_())