print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

class ATM:#Tạo lớp ATM: Lớp này mô phỏng hoạt động của một máy ATM, bao gồm các chức năng như kiểm tra số dư, rút tiền, gửi tiền và xác thực mã PIN.
    def __init__(self):
    #Đây là hàm khởi tạo (__init__) của lớp ATM
        self.balance = 10000  #self.balance = 10000: Khởi tạo số dư tài khoản là 10,000 VND.
        self.pin = "1234" #self.pin = "1234": Khởi tạo mã PIN mặc định là "1234".
    def authenticate(self):# Phương thức authenticate này kiểm tra mã PIN của người dùng:
        attempts = 3 #attempts = 3: Người dùng có 3 lần thử để nhập mã PIN đúng. 
        while attempts > 0:
            #vòng lặp while: Cho phép người dùng nhập mã PIN tối đa 3 lần. 
            entered_pin = input("Nhập mã PIN của bạn: ")
            if entered_pin == self.pin: #Nếu đúng, hiển thị "Mã PIN hợp lệ." và trả về True.
                print("Mã PIN hợp lệ.")
                return True
            else:
                attempts -= 1#Nếu mã PIN sai, giảm số lần thử (attempts -= 1) và yêu cầu người dùng thử lại.
                print(f"Mã PIN sai. Bạn còn {attempts} lần thử.")
        print("Quá số lần thử. Thử lại sau.")
        #Nếu nhập sai hết 3 lần, in ra thông báo "Quá số lần thử. Thử lại sau." và trả về False.
        return False
    def check_balance(self):#Phương thức check_balance sẽ in ra số dư tài khoản của người dùng.
        print(f"Số dư tài khoản của bạn là: {self.balance} VND")
    def withdraw(self):#Phương thức withdraw cho phép người dùng rút tiền:
        amount = float(input("Nhập số tiền bạn muốn rút: "))
        #input(...): Hiển thị dòng nhắc và nhận dữ liệu người dùng nhập vào (kiểu chuỗi).
        #float(...): Chuyển chuỗi đó thành số thực (để cho phép nhập số như 1000.5).
        #amount: Biến chứa số tiền mà người dùng muốn rút.
        if amount <= self.balance:#Nếu số tiền rút nhỏ hơn hoặc bằng số dư hiện tại, thì cho phép rút tiền.
            self.balance -= amount #Trừ số tiền đã rút khỏi số dư và Cập nhật lại số dư tài khoản sau khi rút.
            print(f"Bạn đã rút {amount} VND. Số dư còn lại là: {self.balance} VND.")
        else:#Nếu số tiền muốn rút lớn hơn số dư, không cho phép rút và in ra cảnh báo.
            print("Số dư không đủ để thực hiện giao dịch này.")
    def deposit(self):# Đây là định nghĩa một phương thức có tên deposit trong lớp ATM.Chức năng của nó là cho phép người dùng gửi thêm tiền vào tài khoản.
        amount = float(input("Nhập số tiền bạn muốn gửi: "))
        ##input(...): Hiển thị dòng nhắc và nhận dữ liệu người dùng nhập vào (kiểu chuỗi).
        #float(...): Chuyển chuỗi đó thành số thực (để cho phép nhập số như 1000.5).
        #amount: Biến chứa số tiền mà người dùng muốn gửi.
        self.balance += amount#cộng số tiền đã gửi  và Cập nhật lại số dư tài khoản sau khi gửi.
        print(f"Bạn đã gửi {amount} VND. Số dư hiện tại là: {self.balance} VND.")
    def start(self):# Đây là định nghĩa một phương thức có tên start thuộc lớp ATM. Phương thức này đóng vai trò là điểm khởi đầu của chương trình, nơi người dùng bắt đầu tương tác với máy ATM.
        if not self.authenticate():
        #self.authenticate()Gọi phương thức authenticate() để yêu cầu người dùng nhập mã PIN.
        #if not self.authenticate():Dịch ra: "nếu người dùng không xác thực thành công", tức nhập sai mã PIN.not True → False → tiếp tục chương trình
            return
            #Thoát khỏi hàm start, không cho phép tiếp tục sử dụng ATM.
        while True:
        # Vòng lặp vô hạn (cho phép người dùng thực hiện nhiều thao tác):In ra các lựa chọn cho người dùng: kiểm tra số dư, rút tiền, gửi tiền, hoặc thoát.
            print("\nChọn một chức năng:")
            print("1. Kiểm tra số dư")
            print("2. Rút tiền")
            print("3. Gửi tiền")
            print("4. Thoát")
            choice = input("Nhập lựa chọn của bạn: ")
            if choice == '1':#Nếu lựa chọn là '1', gọi phương thức check_balance().
                self.check_balance()
            elif choice == '2':#Nếu lựa chọn là '2', gọi phương thức withdraw().
                self.withdraw()
            elif choice == '3':#Nếu lựa chọn là '3', gọi phương thức deposit().
                self.deposit()
            elif choice == '4':#Nếu lựa chọn là '4', in thông báo và thoát khỏi vòng lặp (kết thúc giao dịch)
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Hẹn gặp lại!")
                break
            else:#Nếu lựa chọn không hợp lệ, thông báo yêu cầu thử lại.
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
if __name__ == "__main__":#Phần này kiểm tra nếu đoạn mã này đang được chạy trực tiếp (chứ không phải được import).
    atm = ATM()#Tạo một đối tượng atm từ lớp ATM.
    atm.start()#Gọi phương thức start() để bắt đầu giao dịch ATM.
