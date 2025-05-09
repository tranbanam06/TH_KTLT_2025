print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
n = int(input('Nhập số  n: '))
#input(...): Hiện thông báo và yêu cầu người dùng nhập một giá trị từ bàn phím.
#int(...): chuyển kiểu dữ liệu từ chuỗi (mà input trả về) sang số nguyên.
def tong_uoc(x):
#định nghĩa một hàm có tên tong_uoc,Hàm này dùng để tính tổng các ước số thực của số x
    tong = 0 
    #Khởi tạo biến tong để cộng dồn tổng các ước của x
    for i in range(1, x):
    #Vòng lặp này chạy từ từ 1 đến x - 1 (vì range(1, x) không bao gồm x)
        if x % i == 0: 
        #Kiểm tra nếu i là ước của x (tức là x chia hết cho i),Nếu đúng, tức là i là một ước thực 
            tong += i
            #Nếu đúng là ước, thì cộng i vào biến tong
    return tong
    #Sau khi đã duyệt hết các số từ 1 đến x - 1, trả về tổng các ước số thực sự của x
for x in range(1, n):
#Duyệt các số từ 1 đến n - 1
    if tong_uoc(x) > x:
    #Gọi hàm tong_uw(x) để tính tổng các ước của x,So sánh: Nếu tổng các ước lớn hơn chính số x → thì thảo mãn
        print(x)
