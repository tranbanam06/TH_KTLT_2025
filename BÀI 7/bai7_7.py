print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def count_lines_in_file(fname):
#Định nghĩa hàm count_lines_in_file nhận vào một đối số fname là tên hoặc đường dẫn tệp.
    with open(fname, 'r') as file:
    #Mở tệp ở chế độ đọc ('r'), sử dụng mã hóa UTF-8 để đảm bảo đọc được tiếng Việt và ký tự đặc biệt.
    #Câu lệnh with giúp tự động đóng tệp sau khi đọc xong, tránh rò rỉ tài nguyên.
        lines = file.readlines()
        #Đọc toàn bộ nội dung tệp, mỗi dòng là một phần tử trong danh sách lines.
        num_lines = len(lines)
        #Dùng len() để đếm số phần tử trong danh sách lines, tức là số dòng trong tệp.
        return num_lines#Trả về số dòng đã đếm được.
file_name = 'nam.txt' #Gán tên tệp cần đọc vào biến file_name.
line_count = count_lines_in_file(file_name)#Gọi hàm count_lines_in_file để đếm số dòng trong tệp, lưu kết quả vào biến line_count.
print(f"Số dòng trong tệp '{file_name}' là: {line_count}")
