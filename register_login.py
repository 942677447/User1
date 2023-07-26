import sys

from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit

class Registration(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Registration")
        self.setFixedSize(250,250)
        self.setStyleSheet("background: grey")
        self.initUI()
        self.show()

    def initUI(self):
        
        self.expression = ''
        
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.label_login = QLabel()
        self.label_Password = QLabel()

        self.edit_login = QLineEdit()
        self.edit_Password = QLineEdit()

        self.label_login.setText('Login      ')
        self.edit_login.setPlaceholderText('Enter login...')
        self.label_Password.setText('Password')
        self.edit_Password.setPlaceholderText('Enter password...')

        self.btn_ex = QPushButton('Clear')
        self.btn_log = QPushButton('Login')
        self.btn_Reg = QPushButton('Register')

        self.h_box1.addWidget(self.label_login)
        self.h_box1.addWidget(self.edit_login)

        self.h_box2.addWidget(self.label_Password)
        self.h_box2.addWidget(self.edit_Password)

        self.h_box3.addWidget(self.btn_ex)
        self.h_box3.addWidget(self.btn_log)
        self.h_box3.addWidget(self.btn_Reg)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)

        self.btn_ex.setStyleSheet("background: red")
        self.btn_log.setStyleSheet("background: lightgreen")
        self.btn_Reg.setStyleSheet("background: blue")
        self.edit_login.setStyleSheet("background: darkgrey")
        self.edit_Password.setStyleSheet("background: darkgrey")

        self.setLayout(self.v_box)

        self.btn_ex.clicked.connect(self.press_Exit)
        self.btn_Reg.clicked.connect(self.press_register)
        self.btn_log.clicked.connect(self.press_Login)

    def press_Exit(self):
        self.edit_login.clear()
        self.edit_Password.clear()
    
    def press_register(self):
        with open("data.txt","w") as f:
            f.write(f"Login:{self.edit_login.text().ljust(10)}| Password:{self.edit_Password.text().ljust(10)}\n")
            print("Code saved")

    def press_Login(self):
        with open("data.txt","r") as f:
            file = f.read().split()
            print(True)
        


app = QApplication([])
win = Registration()
sys.exit(app.exec_())


