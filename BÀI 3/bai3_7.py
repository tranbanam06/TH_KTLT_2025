def checkValue(n):
#def là từ khóa để định nghĩa một hàm
#checkValue là tên hàm
#(n) là tham số truyền vào hàm – ở đây là một số nguyên
    if n%2==0:#if là lệnh điều kiện (nếu)
    #n % 2 là phép chia lấy dư của n cho 2,nếu dư là 0 (== 0) thì n là số chẵn
        print("Đây là số chẵn") #Nếu điều kiện ở if đúng thì lệnh này sẽ in ra thông báo "Đây là số chẵn"
    else:#Nếu điều kiện if sai (tức là n % 2 != 0), thì khối lệnh trong else sẽ được thực hiện.
        print("Đây là số lẻ")
checkValue(7)#Gọi hàm checkValue với đối số là 7,Vì 7 là số lẻ, nên màn hình sẽ in: "Đây là số lẻ"
print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
