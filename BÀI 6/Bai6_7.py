print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

import math
#Thư viện math được nhập vào.Thư viện này cung cấp các hàm toán học hữu ích, ví dụ như math.pi để lấy giá trị của số pi (π), hay các hàm như sqrt() để tính căn bậc hai, v.v.
class Circle:
#Đây là khai báo lớp (class) có tên là Circle.
#Lớp này đại diện cho một hình tròn, và sẽ chứa các phương thức để tính toán diện tích và chu vi của hình tròn.
    def __init__(self, radius):
    #Đây là hàm khởi tạo (__init__) của lớp Circle.
    #Khi tạo một đối tượng từ lớp này, cần truyền vào giá trị bán kính radius.
        self.radius = radius 
        #self.radius = radius sẽ lưu giá trị bán kính vào thuộc tính radius của đối tượng.
    def area(self):
    #Phương thức area(self) tính diện tích hình tròn:
        return math.pi * self.radius **  2
        #math.pi trả về giá trị của π (3.14159...).
        #self.radius ** 2 tính bình phương của bán kính (r²).
    def circumference(self):
    #circumference(self) tính chu vi hình tròn
        return 2 * math.pi * self.radius
radius = float(input("Nhập bán kính hình tròn: "))
#Dòng này yêu cầu người dùng nhập vào bán kính của hình tròn và lưu giá trị này vào biến radius.
#float() chuyển chuỗi nhập vào thành kiểu dữ liệu số thực (float), vì bán kính có thể là số thập phân.
circle = Circle(radius)
#Tạo một đối tượng circle từ lớp Circle, truyền vào giá trị radius mà người dùng đã nhập vào.
#Đối tượng này sẽ lưu giá trị bán kính và sử dụng các phương thức như area() và circumference()
print(f"Diện tích hình tròn: {circle.area():.2f}")
#:.2f là định dạng để in ra 2 chữ số thập phân sau dấu chấm.
print(f"Chu vi hình tròn: {circle.circumference():.2f}")
