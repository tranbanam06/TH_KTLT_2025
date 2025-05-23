print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import math #Dùng để truy cập các hàm và hằng số toán học như:math.pi: số π (3.14159...),math.sqrt(), v.v.
def Tinh(R):#Khai báo một hàm tên là Tinh, nhận vào một tham số R là bán kính hình tròn
    """Kiểm tra giá trị bán kính"""
    if R <= 0:#Nếu bán kính nhỏ hơn hoặc bằng 0, hàm sẽ trả về thông báo lỗi và không tính tiếp
        return "Giá trị bán kính không hợp lệ. Bán kính phải lớn hơn 0."
    # Tính chu vi và diện tích
    C = 2 * math.pi * R
    S = math.pi * R**2
    return f"Chu vi: {C:.2f}, Diện tích: {S:.2f}" 
    #Trả về một chuỗi định dạng f-string làm tròn chu vi đến 2 chữ số sau dấu phẩy

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính R: "))#kiểu float vì bán kính có thể là số thực
    print(Tinh(R))#Gọi hàm Tinh(R) và in ra kết quả
except ValueError:
#Nếu người dùng nhập chữ hoặc ký tự không phải số,chương trình sẽ không bị lỗi mà in ra thông báo cảnh báo
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số.")
