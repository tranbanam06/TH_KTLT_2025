import re
def check_password(mk):
    if len(mk) < 6 or len(mk) > 12:
        return False
    if not re.search("[a-z]", mk):
        return False
    if not re.search("[A-Z]", mk):
        return False
    if not re.search("[0-9]", mk):
        return False
    if not re.search("[$#@]", mk):
        return False
    return True
passwords=input("Nhap cac mat khau: ").split(',')
valid_passwords = []
for mk in passwords:
    mk = mk.strip() 
    if check_password(mk):
        valid_passwords.append(mk)
if valid_passwords:
    print("Cac mat khau hop le la:", ", ".join(valid_passwords))
else:
    print("Khong co mat khau hop le nao.")
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")
