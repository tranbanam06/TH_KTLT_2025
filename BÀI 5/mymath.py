## File: mymath.py ## 
def square(n): 
# Định nghĩa một hàm tên là square, nhận một tham số đầu vào n
    return n*n 
    #Trả về bình phương của n (n nhân với chính nó)
def cube(n): 
#Định nghĩa hàm cube, nhận một tham số n
    return n*n*n 
    #Trả về lập phương của n (n nhân n nhân n)
def average(values): 
#Định nghĩa một hàm tên là average nhận đầu vào là values, một danh sách các số
    nvals = len(values)
    sum = 0.0
    #Khởi tạo biến sum với giá trị 0.0 (kiểu số thực) để dùng để cộng dồn
    for v in values: 
    #Vòng lặp for để duyệt qua từng phần tử v trong danh sách values.
        sum += v
        #Cộng từng giá trị v vào biến sum  
    return float(sum)/nvals
    #Chia tổng sum cho số phần tử trong danh sách (len(values)) để tính trung bình cộng