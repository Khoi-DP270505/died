import csv

class NetCafeSystem:
    def __init__(self):
        self.users = []
        self.pcs = []
        self.services = []
        self.load_users()
        self.load_pcs()  # Gọi hàm load_pcs để tải thông tin máy từ CSV
        self.load_services()

    # Hàm load người dùng từ CSV
    def load_users(self):
        try:
            with open('data/users.csv', mode='r') as file:
                reader = csv.DictReader(file)
                self.users = list(reader)
        except FileNotFoundError:
            self.users = []

    # Hàm load PC từ CSV
    def load_pcs(self):
        try:
            with open('data/pcs.csv', mode='r') as file:
                reader = csv.DictReader(file)
                self.pcs = list(reader)
        except FileNotFoundError:
            self.pcs = []

    # Hàm load dịch vụ từ CSV
    def load_services(self):
        try:
            with open('data/services.csv', mode='r') as file:
                reader = csv.DictReader(file)
                self.services = list(reader)
        except FileNotFoundError:
            self.services = []

    # Hàm xác thực người dùng khi đăng nhập
    def authenticate(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return user  # Trả về thông tin người dùng
        return None

    # Hàm kiểm tra tên người dùng có tồn tại không
    def username_exists(self, username):
        for user in self.users:
            if user["username"] == username:
                return True
        return False

    # Hàm đăng ký người dùng mới
    def register_user(self, username, password):
        user = {"username": username, "password": password, "balance": "0", "is_admin": "False"}
        self.users.append(user)
        self.save_user(user)

    # Hàm lưu người dùng mới vào file CSV
    def save_user(self, user):
        with open('data/users.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password", "balance", "is_admin"])
            writer.writerow(user)

    # Hàm lưu toàn bộ người dùng vào CSV
    def save_all_users(self):
        with open('data/users.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password", "balance", "is_admin"])
            writer.writeheader()
            writer.writerows(self.users)

    # Hàm lấy thông tin máy mà người dùng đang sử dụng
    def get_user_pc(self, username):
        for pc in self.pcs:
            if pc["username"] == username:
                return pc
        return None

    # Hàm cập nhật trạng thái của PC
    def update_pc_status(self, pc_id, new_status, username=""):
        for pc in self.pcs:
            if pc["pc_id"] == pc_id:
                pc["status"] = new_status
                pc["username"] = username  # Gán tên người dùng vào máy
                break
        self.save_all_pcs()

    # Hàm lưu lại toàn bộ thông tin PC
    def save_all_pcs(self):
        with open('data/pcs.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["pc_id", "pc_type", "status", "username"])
            writer.writeheader()
            writer.writerows(self.pcs)
