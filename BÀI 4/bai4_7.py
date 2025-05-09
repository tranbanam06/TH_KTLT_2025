print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
chuoi = input('Nhap chuoi: ')
#Lệnh input() yêu cầu người dùng nhập một chuỗi từ bàn phím,chuỗi sẽ được lưu vào biến chuoi
chuoi_moi = ''.join([ki_tu for ki_tu in chuoi if not ki_tu.isdigit()])
print('Chuoi sau khi loai b chu so:', chuoi_moi)
