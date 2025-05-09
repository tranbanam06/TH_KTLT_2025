print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
ds = input('Danh sach:').split()
#input('Danh sach:'): Yêu cầu người dùng nhập dữ liệu
#.split() sẽ tách chuỗi vừa nhập thành các phần tử, dựa vào khoảng trắng
ds.reverse()#Hàm reverse() đảo ngược thứ tự phần tử trong danh sách ngay tại chỗ (không tạo danh sách mới)
print(' '.join(ds))
#join(ds) sẽ nối các phần tử trong danh sách thành một chuỗi duy nhất, cách nhau bằng dấu cách ' '
