print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import numpy as np
#Nhập thư viện NumPy với tên viết tắt là np
data = np.array([('James', 5, 48.5), 
                 ('Nail', 6, 52.5), 
                 ('Paul', 5, 42.1), 
                 ('Pit', 5, 40.11)],
                dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])
#Tạo một mảng có cấu trúc gồm 4 bản ghi (hàng), mỗi bản ghi gồm 3 trường (cột):
#'name': tên học sinh – kiểu chuỗi Unicode dài tối đa 10 ký tự ('U10')
#'class': lớp – kiểu số nguyên 32-bit ('i4')
#'height': chiều cao – kiểu số thực 32-bit ('f4')
sorted_data = np.sort(data, order=['class', 'height'])
#Sắp xếp mảng data theo thứ tự ưu tiên:
#Trường 'class' tăng dần
#Nếu 'class' bằng nhau thì sắp tiếp theo 'height' tăng dần
print(sorted_data)
