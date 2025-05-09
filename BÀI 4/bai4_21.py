print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def chia_het_cho_5(binary_str):
#Định nghĩa một hàm tên là chia_het_cho_5, nhận vào một chuỗi nhị phân (binary_str)
    decimal = int(binary_str, 2)
    #Chuyển chuỗi nhị phân sang số thập phân
    return decimal % 5 == 0
    #Trả về True nếu số đó chia hết cho 5, ngược lại là False
input_str = input("Nhập chuỗi các số nhị phân 4 chữ số (phân tách bởi dấu phẩy): ")
#Dòng này yêu cầu người dùng nhập một chuỗi nhiều số nhị phân, cách nhau bằng dấu phẩy
binary_numbers = input_str.split(',')
#.split(',') sẽ tách chuỗi thành danh sách các chuỗi nhị phân
result = [binary for binary in binary_numbers if chia_het_cho_5(binary)]
# lọc ra các số nhị phân chia hết cho 5 bằng cách gọi hàm chia_het_cho_5()
if result:
    print(",".join(result))
    #Nếu danh sách result không rỗng → in ra các số nhị phân đó, cách nhau bằng dấu phẩy
else:
    print("Không có số nhị phân nào chia hết cho 5.")
