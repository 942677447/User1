import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout

class Mywindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(1000,600,350,250)
        self.setWindowTitle('Add Contacts')

        self.v_box = QVBoxLayout(self)

        self.label_name = QLabel(self)
        self.label_name.setText('First name')
        self.v_box.addWidget(self.label_name)

        self.edit_name = QLineEdit(self)
        self.v_box.addWidget(self.edit_name)

        self.label_surname = QLabel(self)
        self.label_surname.setText('Last name')
        self.v_box.addWidget(self.label_surname)

        self.edit_surname = QLineEdit(self)
        self.v_box.addWidget(self.edit_surname)
        
        self.label_number = QLabel(self)
        self.label_number.setText('Phone number')
        self.v_box.addWidget(self.label_number)

        self.edit_phone = QLineEdit(self)
        self.v_box.addWidget(self.edit_phone)

        self.btn = QPushButton(self)
        self.btn.setText('Add New Contact')
        self.v_box.addWidget(self.btn)

        self.setLayout(self.v_box)
        
        self.btn.clicked.connect(self.press)

        self.show()

    def press(self):
        print(self.edit_name.text())
        print(self.edit_surname.text())
        print(self.edit_phone.text())
        self.edit_name.clear()
        self.edit_surname.clear()
        self.edit_phone.clear()

app = QApplication([])
win = Mywindow()

sys.exit(app.exec_())

        