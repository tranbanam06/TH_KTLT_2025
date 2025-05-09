l=input("Nhap danh sach l: ").split(',')
k=input("Nhap danh sach k: ").split(',')
#Chuyen doi cac phan tu so tu chuoi sang kieu so nguyen neu co the
l=[int(x) if x.isdigit() else x for x in l]
k=[int(x) if x.isdigit() else x for x in k]
m=[]
m.append(l);
m.append(k);
print(m)
d={1:l,2:k,'combine_list' :m}
print(d)
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")