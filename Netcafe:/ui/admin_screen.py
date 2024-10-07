from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit
from csv_backend import NetCafeSystem

class AdminScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.cafe = NetCafeSystem()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Quản lý Quán Net (Admin)")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Nút quản lý PC
        button_manage_pcs = QPushButton('Gán người dùng vào máy trạm')
        button_manage_pcs.clicked.connect(self.assign_user_to_pc)
        layout.addWidget(button_manage_pcs)

        self.setLayout(layout)

    def assign_user_to_pc(self):
        pc_window = QWidget()
        pc_window.setWindowTitle("Gán Người Dùng Vào Máy Trạm")
        pc_window.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(len(self.cafe.pcs))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Loại máy", "Trạng thái", "Người dùng"])

        for i, pc in enumerate(self.cafe.pcs):
            table.setItem(i, 0, QTableWidgetItem(pc['pc_id']))
            table.setItem(i, 1, QTableWidgetItem(pc['pc_type']))
            table.setItem(i, 2, QTableWidgetItem(pc['status']))
            table.setItem(i, 3, QTableWidgetItem(pc['username']))

        layout.addWidget(table)
        
        # Thêm ô nhập tên người dùng
        username_input = QLineEdit(pc_window)
        username_input.setPlaceholderText("Nhập tên người dùng")
        layout.addWidget(username_input)

        def assign_user():
            selected_pc_id = table.currentRow() + 1
            username = username_input.text()

            if not username:
                QMessageBox.warning(pc_window, 'Lỗi', 'Bạn cần nhập tên người dùng')
                return

            selected_pc = self.cafe.pcs[selected_pc_id - 1]
            if selected_pc["status"] == "available":
                self.cafe.update_pc_status(str(selected_pc_id), "in-use", username)
                QMessageBox.information(pc_window, 'Thành công', f"Gán {username} vào máy {selected_pc_id}")
            else:
                QMessageBox.warning(pc_window, 'Lỗi', f"Máy {selected_pc_id} đang được sử dụng")

        button_confirm = QPushButton('Xác nhận gán người dùng')
        button_confirm.clicked.connect(assign_user)
        layout.addWidget(button_confirm)

        pc_window.setLayout(layout)
        pc_window.show()
