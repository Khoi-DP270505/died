from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from ui.main_screen import MainScreen
from ui.admin_screen import AdminScreen  # Thêm màn hình quản lý cho admin
from csv_backend import NetCafeSystem
from ui.register import RegisterWindow  # Thêm cửa sổ đăng ký

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Đăng nhập")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label_username = QLabel('Tên đăng nhập:')
        self.entry_username = QLineEdit(self)

        self.label_password = QLabel('Mật khẩu:')
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton('Đăng nhập', self)
        self.button_login.clicked.connect(self.login)

        self.button_register = QPushButton('Đăng ký', self)
        self.button_register.clicked.connect(self.open_register_window)  # Mở cửa sổ đăng ký

        layout.addWidget(self.label_username)
        layout.addWidget(self.entry_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_register)

        self.setLayout(layout)

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        cafe = NetCafeSystem()
        user = cafe.authenticate(username, password)
        if user:
            if user["is_admin"] == 'True':  # Kiểm tra xem có phải admin không
                QMessageBox.information(self, 'Thành công', 'Đăng nhập thành công! Chào mừng Admin!')
                self.admin_screen = AdminScreen()  # Mở màn hình quản lý cho admin
                self.admin_screen.show()
            else:
                QMessageBox.information(self, 'Thành công', 'Đăng nhập thành công! Chào mừng bạn!')
                self.main_screen = MainScreen(username)  # Mở màn hình chính cho người dùng
                self.main_screen.show()
            self.close()  # Đóng cửa sổ đăng nhập
        else:
            QMessageBox.warning(self, 'Lỗi', 'Sai tên đăng nhập hoặc mật khẩu!')

    def open_register_window(self):
        self.register_window = RegisterWindow()  # Tạo cửa sổ đăng ký
        self.register_window.show()  # Hiển thị cửa sổ đăng ký
