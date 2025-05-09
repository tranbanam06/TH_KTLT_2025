print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

def sequential_search(dlist, item):
    for i in range(len(dlist)):
    #Vòng lặp for duyệt từng phần tử trong dlist theo chỉ số i.
        if dlist[i] == item:
        #Nếu tìm thấy phần tử tại dlist[i] == item, trả về True và chỉ số i
            return (True, i)
    return (False, -1)
    #duyệt hết mà không tìm thấy, trả về False và -1
if __name__ == "__main__":
#Câu lệnh này đảm bảo đoạn mã bên dưới chỉ chạy khi file được thực thi trực tiếp, không chạy khi nó bị import từ file khác
    dlist = list(map(int, input("Nhập dãy số (các số cách nhau bằng dấu cách): ").split()))
   #Dùng input() để lấy chuỗi từ bàn phím.
    #split() tách chuỗi thành các phần tử dựa theo dấu cách.
    #map(int, ...) chuyển từng phần tử sang số nguyên.
    #list(...) chuyển kết quả thành danh sách.
    item = int(input("Nhập phần tử cần tìm: "))
    #Nhập một số nguyên từ bàn phím để tìm kiếm trong danh sách
    result = sequential_search(dlist, item)
    #Gọi hàm sequential_search với danh sách và phần tử cần tìm
    if result[0]:
    #Kiểm tra result[0] (giá trị True hoặc False)
        print(f"Phần tử {item} được tìm thấy tại chỉ mục {result[1]}.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")
