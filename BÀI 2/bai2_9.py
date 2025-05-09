str = input("Nhap mot chuoi: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")