print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
ds = input('Danh sach:').split()
#input('Danh sach:'): Yêu cầu người dùng nhập dữ liệu
#.split() sẽ tách chuỗi vừa nhập thành các phần tử, dựa vào khoảng trắng
print(ds)#In toàn bộ danh sách ds ra dưới dạng list Python
for so in  ds:#Dùng vòng lặp for để duyệt từng phần tử trong danh sách ds
    print(so) #Biến so sẽ lần lượt nhận từng giá trị trong danh sách và in ra
