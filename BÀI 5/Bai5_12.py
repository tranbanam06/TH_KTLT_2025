print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

import numpy as np
#Nhập thư viện NumPy để thao tác với mảng.
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
##student_id: Mảng mã số sinh viên.
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])
#student_height: Mảng chiều cao tương ứng với từng sinh viên.
sorted_indices = np.lexsort((student_height, student_id))
#Hàm np.lexsort() trong NumPy dùng để sắp xếp theo nhiều khóa (nhiều tiêu chí)
#np.lexsort() nhận một tuple các mảng, sắp xếp theo thứ tự ưu tiên từ trái sang phải (ưu tiên cuối cùng bên trái).
#nó sắp xếp theo chiều cao trước, nếu chiều cao bằng nhau thì xét đến student_id.
print("Chỉ số:")
print(sorted_indices)
print("\nDữ liệu sắp xếp:")
for idx in sorted_indices:
    print(f"{student_id[idx]} \t {student_height[idx]}")
