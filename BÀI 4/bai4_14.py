print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
ds = input('Nhap chuoi:').split()
#input(...): yêu cầu người dùng nhập một dòng văn bản.
#.split(): tách chuỗi đó thành các phần tử (tách theo khoảng trắng).
ds.sort()
#được dùng để sắp xếp danh sách ds theo thứ tự tăng dần (chữ cái A → Z, số nhỏ → lớn).
#.sort() sẽ sắp xếp danh sách ngay tại chỗ (in-place), tức là thay đổi luôn danh sách gốc
for ch in ds:
#Duyệt qua từng phần tử trong danh sách ds
    print(ch)
    #In từng phần tử ra mỗi dòng một từ
