print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def in_tam_giac_pascal(n):
#Khai báo hàm, nhận vào n là số dòng của tam giác Pascal
    for i in range(n):
    #Tạo vòng lặp từ dòng 0 đến dòng n-1
        hang = [1] * (i + 1)
        #Tạo danh sách hang có i + 1 phần tử, tất cả đều là 1,Vì trong Pascal, đầu và cuối mỗi hàng luôn là 1
        for j in range(1, i):
        #Lặp qua các vị trí giữa dòng (trừ đầu và cuối), để tính giá trị theo công thức Pascal
            hang[j] = prev_row[j - 1] + prev_row[j]
            #Cập nhật các giá trị giữa của dòng hiện tại, dựa vào dòng trước (prev_row)
        print(' '.join(map(str, hang)))
        #In ra dòng hiện tại, chuyển từng số thành chuỗi rồi nối bằng dấu cách.
        prev_row = hang
        #Gán dòng hiện tại thành prev_row để dùng cho dòng sau.
n = int(input('Nhap so nguyen n: '))
in_tam_giac_pascal(n)
