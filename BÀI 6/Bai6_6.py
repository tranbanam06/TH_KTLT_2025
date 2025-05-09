print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

class StringManipulator:
# Đây là khai báo lớp (class) tên là StringManipulator
#Lớp này có nhiệm vụ xử lý và thao tác với chuỗi, ví dụ như nhận chuỗi từ người dùng và in ra chuỗi đó ở dạng in hoa.
    def __init__(self):
    # Đây là hàm khởi tạo (__init__) của lớp StringManipulator.
    # #self là tham chiếu đến đối tượng của lớp hiện tại. Điều này cho phép bạn truy cập vào thuộc tính và phương thức của đối tượng.
        self.user_string = ""  
        #Khi bạn tạo đối tượng từ lớp này, self.user_string = "" sẽ khởi tạo một biến user_string rỗng (chuỗi trống).
    def get_String(self):
    #Đây là phương thức (hàm) get_String dùng để nhận chuỗi từ người dùng.
        self.user_string = input("Nhập một chuỗi: ")
        #input("Nhập một chuỗi: ") sẽ hiển thị một thông báo yêu cầu người dùng nhập một chuỗi.Chuỗi người dùng nhập sẽ được gán vào biến user_string.
    def print_String(self):
    #Đây là phương thức (hàm) print_String dùng để in ra chuỗi ở dạng in hoa.
        print(self.user_string.upper())
        #self.user_string.upper() sẽ chuyển tất cả các ký tự trong chuỗi user_string thành in hoa và in ra
manipulator = StringManipulator()
#Tạo một đối tượng từ lớp StringManipulator.Đối tượng này được gọi là manipulator
manipulator.get_String()
#Gọi phương thức get_String() từ đối tượng manipulator
manipulator.print_String()
#Gọi phương thức print_String() từ đối tượng manipulator