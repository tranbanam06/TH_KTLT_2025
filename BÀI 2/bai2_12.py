import re #Dùng thư viện re để sử dụng biểu thức chính quy (regex)
def check_password(mk): #Hàm này dùng để kiểm tra một mật khẩu có hợp lệ không.
    if len(mk) < 6 or len(mk) > 12: #Kiểm tra độ dài mật khẩu phải từ 6 đến 12 ký tự.
        return False
    if not re.search("[a-z]", mk): #Kiểm tra phải có ít nhất một chữ thường
        return False
    if not re.search("[A-Z]", mk): #Kiểm tra phải có ít nhất một chữ hoa
        return False 
    if not re.search("[0-9]", mk): #Kiểm tra phải có ít nhất một chữ số
        return False
    if not re.search("[$#@]", mk): #Kiểm tra phải có ít nhất một trong các ký tự đặc biệt: $, #, hoặc @
        return False
    return True
passwords=input("Nhap cac mat khau: ").split(',') #êu cầu người dùng nhập nhiều mật khẩu, ngăn cách bằng dấu ,
valid_passwords = []
for mk in passwords:
    mk = mk.strip()  #Dùng .strip() để xóa khoảng trắng dư thừa đầu/cuối từng mật khẩu.
    if check_password(mk): #Nếu hàm check_password() trả về True, thì thêm mk vào danh sách hợp lệ.
        valid_passwords.append(mk)
if valid_passwords:
    print("Cac mat khau hop le la:", ", ".join(valid_passwords))
else:
    print("Khong co mat khau hop le nao.")
    #Nếu danh sách có mật khẩu hợp lệ → in ra
    #Nếu không có mật khẩu nào hợp lệ → thông báo
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")
