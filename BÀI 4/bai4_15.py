print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
chuoi = input('Nhập chuỗi cac tu tieng anh: ')
#input(...): yêu cầu người dùng nhập một dòng văn bản.
ds_list = chuoi.split()
#.split(): tách chuỗi đó thành các phần tử (tách theo khoảng trắng)
ds_list.sort()
#được dùng để sắp xếp danh sách ds theo thứ tự tăng dần (chữ cái A → Z, số nhỏ → lớn).
#.sort() sẽ sắp xếp danh sách ngay tại chỗ (in-place), tức là thay đổi luôn danh sách gốc
print('cac tu theo thu tu tu dien:')
for tu in ds_list:
#Duyệt từng phần tử (tức là từng từ) trong danh sách ds_list
    print(tu)
    #In từng từ ra mỗi dòng một từ
