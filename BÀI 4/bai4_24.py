print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
input_str = input("Nhập vào một câu: ")
#Yêu cầu người dùng nhập một câu bất kỳ từ bàn phím.Giá trị người dùng nhập sẽ được lưu vào biến input_str dưới dạng chuỗi (str)
upper_count = 0
#gán biến đếm số chữ cái viết hoa bằng 0
lower_count = 0
##gán biến đếm số chữ cái viết thường bằng 0
for char in input_str:
#Lặp qua từng ký tự char trong chuỗi input_str
    if char.isupper(): 
    #char.isupper() kiểm tra xem ký tự có phải là chữ cái in hoa không,Nếu đúng, cộng thêm 1 vào upper_count 
        upper_count += 1
    elif char.islower():  
    #char.islower() kiểm tra xem ký tự có phải là chữ cái in thường không,Nếu đúng, cộng thêm 1 vào lower_count
        lower_count += 1

print(f"Chữ hoa: {upper_count}")
print(f"Chữ thường: {lower_count}")
