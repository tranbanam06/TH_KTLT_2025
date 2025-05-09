print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
binary_input = input("nhap chuoi cac so nhi phan: ")
#Yêu cầu người dùng nhập một chuỗi gồm nhiều số nhị phân, cách nhau bằng dấu phẩy
binary_values = binary_input.split(',')
#Tách chuỗi thành danh sách các chuỗi nhỏ, cắt theo dấu phẩy
print("cac gia tri nhi phan da nhap:")
for value in binary_values:
#Duyệt từng phần tử value trong danh sách binary_values
    print(value.strip())
    #.strip() dùng để loại bỏ khoảng trắng thừa ở đầu và cuối mỗi chuỗi
