str = input("Nhap mot chuoi: ") 
dict = {} #Tạo một từ điển rỗng (dict) để lưu số lần xuất hiện của từng ký tự.
for n in str: #Duyệt từng ký tự n trong chuỗi đã nhập.
    keys = dict.keys() #Lấy danh sách các khóa hiện tại trong từ điển.
    if n in keys:
        dict[n] += 1 #Nếu ký tự n đã có trong từ điển → tăng giá trị (tức là số lần xuất hiện) thêm 1.
    else:
        dict[n] = 1 #Nếu ký tự n chưa có trong từ điển → thêm vào với giá trị khởi đầu là 1
print (dict) #In ra toàn bộ từ điển, với mỗi ký tự là một khóa, và giá trị là số lần ký tự đó xuất hiện.
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")