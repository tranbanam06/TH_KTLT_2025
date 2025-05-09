print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
n = int(input("Nhập số nguyên n: "))
#input(...): Hiện thông báo và yêu cầu người dùng nhập một giá trị từ bàn phím.
#int(...): chuyển kiểu dữ liệu từ chuỗi (mà input trả về) sang số nguyên.
def fibonacci_lesser_than_n(n):
#Khai báo một hàm tên là fibonacci_lesser_than_n, nhận tham số đầu vào là n vói mục tiêu trả về một danh sách các số Fibonacci nhỏ hơn n
    fib = []
    #Tạo một danh sách rỗng để lưu dãy Fibonacci  
    a, b = 0, 1 
    #Khởi tạo 2 biến đầu tiên của dãy Fibonacci 
    while a < n:
    #Vòng lặp tiếp tục chừng nào a còn nhỏ hơn n, 
        fib.append(a)
        #Mỗi vòng lặp sẽ thêm giá trị a vào danh sách fib
        a, b = b, a + b 
        #Cập nhật 2 số tiếp theo trong dãy Fibonacci.a trở thành b (số tiếp theo), b trở thành a + b (tính tổng 2 số trước đó
    return fib
    #Sau khi vòng lặp kết thúc, trả về danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = fibonacci_lesser_than_n(n)
#Gọi hàm fibonacci_lesser_than_n(n) với giá trị người dùng đã nhập,Kết quả trả về (là danh sách số Fibonacci) được gán vào biến fibonacci_numbers
print(fibonacci_numbers)
