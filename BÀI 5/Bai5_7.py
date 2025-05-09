print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

import numpy as np 
#Nhập thư viện numpy và đặt bí danh là np để sử dụng ngắn gọn
# chú thích: numpy là thư viện mạnh mẽ dùng cho tính toán mảng, ma trận và đại số tuyến tính.
data_type = [('name', 'S15'), ('class', int), ('height', float)] 
#Tạo một biến data_type chứa một danh sách các cặp (tên trường, kiểu dữ liệu), gọi là kiểu dữ liệu có cấu trúc 
#'name': tên sinh viên, dạng chuỗi bytes dài tối đa 15 ký tự ('S15').
#'class': lớp học, kiểu số nguyên.
#'height': chiều cao, kiểu số thực (float).
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)] 
#Tạo danh sách students_details gồm 3 tuple (đại diện cho từng sinh viên), mỗi tuple chứa tên sinh viên (chuỗi)lớp học (số nguyên)chiều cao (số thực).
# create a structured array 
students = np.array(students_details, dtype=data_type)   
#Tạo một mảng có cấu trúc từ danh sách students_details với kiểu dữ liệu đã định nghĩa ở data_type 
print("Original array:") 
print(students) 
print("Sort by height") 
print(np.sort(students, order='height'))
#Sử dụng np.sort() để sắp xếp mảng theo chiều tăng dần của trường 'height'
