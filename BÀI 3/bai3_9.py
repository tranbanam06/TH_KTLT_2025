print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
""" Chương trình hoạt động như một cái máy tính bỏ túi bình thường  có thể cộng trù nhân chia """
# This function adds two numbers  
def tong(x, y): #Đây là hàm cộng hai số x và y.
 return x + y #return trả lại kết quả phép cộng
# This function subtracts two numbers  
def hieu(x, y): 
 return x - y 
# This function multiplies two numbers 
def tich(x, y): 
 return x * y 
# This function divides two numbers 
def thuong(x, y): #Nếu y = 0 sẽ gây lỗi chia cho 0 — chương trình hiện tại chưa xử lý lỗi này
 return x / y 
"""In ra hướng dẫn để người dùng chọn phép tính"""
print("Select operation.") 
print("1.tong") 
print("2.hieu") 
print("3.tich") 
print("4.thuong") 
# Take input from the user  
choice = input("Enter choice(1/2/3/4):") #Nhập số lựa chọn từ người dùng để xác định phép tính
#Nhập hai số nguyên (int) từ người dùng để thực hiện phép tính
num1 = int(input("Vui lòng nhập số đầu tiên: ")) 
num2 = int(input("Vui lòng nhập số thứ hai: ")) 
"""Kiểm tra biến choice để xác định phép tính tương ứng,Nếu nhập sai lựa chọn (choice không phải 1–4), 
chương trình in:Invalid input"""
if choice == '1': 
 print(num1,"+",num2,"=", tong(num1,num2)) 
elif choice == '2': 
 print(num1,"-",num2,"=", hieu(num1,num2)) 
elif choice == '3': 
 print(num1,"*",num2,"=", tich(num1,num2)) 
elif choice == '4': 
 print(num1,"/",num2,"=", thuong(num1,num2)) 
else: 
 print("Invalid input") 
