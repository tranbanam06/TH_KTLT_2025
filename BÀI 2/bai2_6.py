j = []
for i in range (2000, 3201):
    if (i % 7==0) and (i % 5 !=0):
        j.append(str(i)) #Thêm số i vào danh sách j
print (','.join(j)) #Ghép tất cả các phần tử trong danh sách j thành một chuỗi duy nhất, các phần tử cách nhau bằng dấu phẩy ,.

print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")