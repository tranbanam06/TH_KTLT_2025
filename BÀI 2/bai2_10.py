a=input("Nhap mot cau: ")
b=a.split() #Dùng hàm split() để tách câu thành danh sách các từ, dựa theo dấu cách (space).
print (b) #In ra danh sách các từ đã tách.
c=" ".join(b) #Dùng join() để nối lại danh sách b thành chuỗi, mỗi từ cách nhau bởi đúng 1 dấu cách.
print(c) #In ra câu sau khi đã chuẩn hóa khoảng trắng.
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")