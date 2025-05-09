print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
ten_nguoi = input('Nhap ten nguoi (ho va ten): ')
#Yêu cầu người dùng nhập họ và tên từ bàn phím.Dữ liệu nhập vào sẽ được lưu trong biến ten_nguoi
ho, ten = ten_nguoi.split()#.split() sẽ tách chuỗi ten_nguo thành danh sách các từ, ngăn cách bởi dấu cách
"""Lưu ý: nếu người dùng nhập nhiều hơn hoặc ít hơn 2 từ, chương trình sẽ báo lỗi (ValueError),
vì không thể gán đúng số biến"""
print('Ho:', ho)
print('Ten rieng:', ten)
