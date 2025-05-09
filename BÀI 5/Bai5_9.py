print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
# main.py
import binary_search
#Import module binary_search. Module này phải có trong cùng thư mục hoặc có thể truy cập được bởi Python
if __name__ == "__main__":
#Đảm bảo phần dưới chỉ chạy khi file được chạy trực tiếp, không chạy khi import từ nơi khác.
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    #Nhận từ bàn phim số nguyên n đại diện cho số phần tử trong danh sách chuyển nó sang dạng số nguyên
    dlist = list(map(int, input(f"Nhập {n} phần tử (các số cách nhau bằng dấu cách): ").split()))
    #Dùng split() để tách chuỗi theo khoảng trắng, map(int, ...) để chuyển về số nguyên, rồi tạo thành một danh sách dlist
    dlist.sort()
    #Bắt buộc phải sắp xếp danh sách trước khi thực hiện tìm kiếm nhị phân, vì thuật toán yêu cầu danh sách có thứ tự tăng dần.
    value = int(input("Nhập phần tử cần tìm: "))
    #Nhập giá trị cần tìm kiếm từ người dùng.
    result = binary_search.binary_search(dlist, value)
    #Gọi hàm binary_search() từ module binary_search, truyền vào danh sách dlist và giá trị value
    if result:
    #Kiểm tra nếu result có giá trị (không phải None, False hoặc -1
        print(f"Phần tử {value} được tìm thấy trong danh sách.")
    else:
        print(f"Phần tử {value} không có trong danh sách.")
