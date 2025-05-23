l=input("Nhap danh sach l: ").split(',')
k=input("Nhap danh sach k: ").split(',')
#Chuyen doi cac phan tu so tu chuoi sang kieu so nguyen neu co the
l=[int(x) if x.isdigit() else x for x in l]
k=[int(x) if x.isdigit() else x for x in k]
#x.isdigit() kiểm tra xem x có phải là chuỗi số hay không
#Nếu là số → chuyển sang int
#Nếu là chữ (ví dụ 'a', 'b') → giữ nguyên
m=[]
m.append(l);
m.append(k);
#Gộp 2 danh sách lại vào m
print(m)
d={1:l,2:k,'combine_list' :m}
#Tạo từ điển chứa từng danh sách và danh sách gộp
print(d)
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")