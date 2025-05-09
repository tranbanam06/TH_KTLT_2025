print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def read_entire_file(file_path):
#Định nghĩa một hàm có tên là read_entire_file, nhận vào tham số file_path là đường dẫn đến tệp cần đọc.
    try:
    #Bắt đầu một khối try-except để xử lý lỗi (nếu có lỗi khi đọc tệp).
        with open(file_path, 'r', encoding='utf-8') as file:
        #Mở tệp ở chế độ đọc ('r'), sử dụng mã hóa UTF-8 để đảm bảo đọc được tiếng Việt và ký tự đặc biệt.
        #Câu lệnh with giúp tự động đóng tệp sau khi đọc xong, tránh rò rỉ tài nguyên.
        #Biến file đại diện cho tệp đang mở.
            content = file.read() 
            #Đọc toàn bộ nội dung của tệp dưới dạng một chuỗi (str), lưu vào biến content. 
            print(content)  
            #In toàn bộ nội dung tệp ra màn hình, bao gồm cả các ký tự xuống dòng và dấu cách.   
    except FileNotFoundError:
    #Nếu tệp không tồn tại tại đường dẫn đã cho, in ra thông báo lỗi rõ ràng.
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
    #Nếu có lỗi khác (như lỗi mã hóa, quyền truy cập...), in ra thông báo cùng thông tin chi tiết từ biến e.
        print(f"Có lỗi xảy ra: {e}")
read_entire_file('nam.txt')
#Gọi hàm read_entire_file với đường dẫn 'nam.txt' để thực thi và in nội dung tệp.
