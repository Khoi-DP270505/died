from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from csv_backend import NetCafeSystem

class MainScreen(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.cafe = NetCafeSystem()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"Chào mừng {self.username} đến quán net")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Hiển thị thông tin tài khoản
        self.label_welcome = QLabel(f"Chào mừng {self.username}!")
        self.label_balance = QLabel(f"Số dư tài khoản: {self.get_user_balance()} VNĐ")
        self.label_pc = QLabel(f"Bạn đang sử dụng máy: {self.get_user_pc()}")
        layout.addWidget(self.label_welcome)
        layout.addWidget(self.label_balance)
        layout.addWidget(self.label_pc)

        # Thêm phần chọn dịch vụ
        self.label_service = QLabel("Chọn dịch vụ:")
        layout.addWidget(self.label_service)

        self.combo_services = QComboBox(self)
        self.load_services()  # Tải dịch vụ từ CSV
        layout.addWidget(self.combo_services)

        # Nút sử dụng dịch vụ
        button_use_service = QPushButton('Sử dụng dịch vụ', self)
        button_use_service.clicked.connect(self.use_service)
        layout.addWidget(button_use_service)

        # Nút đăng xuất
        button_logout = QPushButton('Đăng xuất', self)
        button_logout.clicked.connect(self.logout)
        layout.addWidget(button_logout)

        self.setLayout(layout)

    def get_user_balance(self):
        for user in self.cafe.users:
            if user["username"] == self.username:
                return user["balance"]
        return 0

    def get_user_pc(self):
        pc = self.cafe.get_user_pc(self.username)
        if pc:
            return f"{pc['pc_id']} (Loại: {pc['pc_type']})"
        return "Bạn chưa ngồi máy nào"

    def load_services(self):
        for service in self.cafe.services:
            service_name = f"{service['service_name']} - {service['price']} VNĐ"
            self.combo_services.addItem(service_name, service['service_id'])

    def use_service(self):
        service_index = self.combo_services.currentIndex()
        selected_service = self.cafe.services[service_index]
        service_price = int(selected_service['price'])

        current_balance = int(self.get_user_balance())

        if current_balance >= service_price:
            new_balance = current_balance - service_price
            self.cafe.update_user_balance(self.username, new_balance)
            self.label_balance.setText(f"Số dư tài khoản: {new_balance} VNĐ")
            QMessageBox.information(self, 'Thành công', f"Bạn đã sử dụng {selected_service['service_name']} với giá {service_price} VNĐ")
        else:
            QMessageBox.warning(self, 'Lỗi', 'Số dư không đủ để sử dụng dịch vụ này!')

    def logout(self):
        self.close()
