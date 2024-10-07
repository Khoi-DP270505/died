from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from csv_backend import NetCafeSystem

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Đăng ký")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.label_reg_username = QLabel('Tên đăng nhập:')
        self.entry_reg_username = QLineEdit(self)

        self.label_reg_password = QLabel('Mật khẩu:')
        self.entry_reg_password = QLineEdit(self)
        self.entry_reg_password.setEchoMode(QLineEdit.Password)

        self.label_confirm_password = QLabel('Nhập lại mật khẩu:')
        self.entry_confirm_password = QLineEdit(self)
        self.entry_confirm_password.setEchoMode(QLineEdit.Password)

        self.button_register = QPushButton('Xác nhận đăng ký', self)
        self.button_register.clicked.connect(self.register)

        layout.addWidget(self.label_reg_username)
        layout.addWidget(self.entry_reg_username)
        layout.addWidget(self.label_reg_password)
        layout.addWidget(self.entry_reg_password)
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.entry_confirm_password)
        layout.addWidget(self.button_register)

        self.setLayout(layout)

    def register(self):
        username = self.entry_reg_username.text()
        password = self.entry_reg_password.text()
        confirm_password = self.entry_confirm_password.text()

        if password != confirm_password:
            QMessageBox.warning(self, 'Lỗi', 'Mật khẩu không khớp!')
        else:
            cafe = NetCafeSystem()
            if cafe.username_exists(username):
                QMessageBox.warning(self, 'Lỗi', 'Tên đăng nhập đã tồn tại!')
            else:
                cafe.register_user(username, password)
                QMessageBox.information(self, 'Thành công', 'Đăng ký thành công!')
                self.close()  # Đóng cửa sổ đăng ký
