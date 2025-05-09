print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

import numpy as np
#Nhập thư viện numpy và đặt bí danh là np để sử dụng ngắn gọn
# chú thích: numpy là thư viện mạnh mẽ dùng cho tính toán mảng, ma trận và đại số tuyến tính.
mang = np.arange(12, 39)
#Tạo một mảng NumPy từ số 12 đến 38 (không bao gồm 39), với bước nhảy mặc định là 1.
print("Mảng ban đầu:",mang)
mang_dao_nguoc = np.flip(mang)
#Dùng hàm np.flip() để đảo ngược thứ tự phần tử trong mảng mang
print("Mảng đảo ngược:", mang_dao_nguoc)
# In ra mảng đã bị đảo ngược