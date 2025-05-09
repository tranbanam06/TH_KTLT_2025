print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
# main.py
import mymodule
#Nhập mô-đun mymodule – một tệp Python khác
n = int(input("Nhập số lượng phần tử của danh sách: "))
#In ra thông báo yêu cầu người dùng nhập số lượng phần tử từ bàn phím và chuyển nó về số.
lst = []
#Khởi tạo một danh sách rỗng có tên là lst để lưu các giá trị người dùng nhập vào
for i in range(n):
#Vòng lặp chạy từ i = 0 đến i = n-1, thực hiện lặp đúng n lần.
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    #Hiển thị thông báo yêu cầu người dùng nhập phần tử thứ i+1 (đếm từ 1 cho dễ nhìn)
    #float() kiểu thành số thực
    lst.append(value)
    #Thêm giá trị vừa nhập vào danh sách lst
max_value = mymodule.find_max(lst)
#Gọi hàm find_max() từ mô-đun mymodule để tìm giá trị lớn nhất trong danh sách lst
min_value = mymodule.find_min(lst)
#Gọi hàm find_min() để tìm giá trị nhỏ nhất trong danh sách
sorted_list = mymodule.sort_list(lst)
#Gọi hàm sort_list() để trả về một danh sách mới đã được sắp xếp tăng dần.
print(f"Phần tử lớn nhất trong danh sách: {max_value}")
print(f"Phần tử nhỏ nhất trong danh sách: {min_value}")
print(f"Danh sách sau khi sắp xếp: {sorted_list}")
