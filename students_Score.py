import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout

from datetime import datetime

class Students(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Students Score')
        self.setFixedSize(230,230)
        self.setStyleSheet("background: lightgrey")
        self.initUI()
        self.show()

    def initUI(self):

        self.count = 0
        
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.v_box = QVBoxLayout()
        
        self.label_name = QLabel()
        self.label_subject = QLabel()
        self.label_count = QLabel()
        
        self.label_name.setText('Name')
        self.label_subject.setText('Subject')
        self.label_count.setText('0')
        
        self.edit_name = QLineEdit()
        self.edit_subject = QLineEdit()
        
        self.edit_name.setPlaceholderText("Enter name...")
        self.edit_subject.setPlaceholderText("Enter subject...")
        
            
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_save = QPushButton("Save")
        self.btn_exit = QPushButton("Exit")
        
        self.btn_save.setStyleSheet("background: red")
        self.btn_exit.setStyleSheet("background: darkblue")


        self.h_box1.addWidget(self.label_name)
        self.h_box1.addWidget(self.edit_name)

        self.h_box2.addWidget(self.label_subject)
        self.h_box2.addWidget(self.edit_subject)

        self.h_box3.addWidget(self.btn_plus)
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.label_count)
        self.h_box3.addStretch()
        self.h_box3.addWidget(self.btn_minus)

        self.h_box4.addWidget(self.btn_save)
        self.h_box4.addWidget(self.btn_exit)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.btn_save.clicked.connect(self.press_save)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_exit.clicked.connect(self.press_exit)

    def plus(self):
        if self.count < 10:
            self.count+=1
        self.label_count.setText(str(self.count))

    def minus(self):
        if self.count > 0:
            self.count-=1
        self.label_count.setText(str(self.count))    
        
    def press_save(self):
        with open("data.txt","a") as file:
            time = datetime.now()
            file.write(f"{self.edit_name.text().ljust(10)}|{self.edit_subject.text().ljust(10)}|{self.label_count.text().ljust(10)}|{time.strftime('%H:%M:%S')}\n")
            print("Data saved fully: ")

    def press_exit(self):
        self.edit_name.clear()
        self.edit_subject.clear()
        self.label_count.clear()
        self.count = 0
        self.label_count.setText(str(self.count))

    
        
       
    
        

app = QApplication([])
win = Students()
sys.exit(app.exec_())