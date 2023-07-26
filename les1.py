import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
 def __init__(self):
  super().__init__()

  self.btn1=QPushButton("+")
  self.btn2=QPushButton("-")
  self.btn3=QPushButton("*")
  self.btn4=QPushButton("/")

  self.h_box1=QHBoxLayout()
  self.h_box2=QHBoxLayout()
  self.h_box3=QHBoxLayout()
  self.v_box=QVBoxLayout()

  self.h_box1.addStretch()
  self.h_box1.addWidget(self.btn1)
  self.h_box1.addStretch()

  self.h_box2.addWidget(self.btn2)
  self.h_box2.addStretch()
  self.h_box2.addWidget(self.btn3)

  self.h_box3.addStretch()
  self.h_box3.addWidget(self.btn4)
  self.h_box3.addStretch()

  self.v_box.addLayout(self.h_box1)
  self.v_box.addLayout(self.h_box2)
  self.v_box.addLayout(self.h_box3)

  self.setLayout(self.v_box)
  



app=QApplication(sys.argv)
win=MyWindow()
win.show()
sys.exit(app.exec())