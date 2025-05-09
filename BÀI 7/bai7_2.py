print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def analyze_file(file_path):
#Định nghĩa một hàm có tên là analyze_file, nhận tham số file_path là đường dẫn đến tệp cần phân tích.
    try:
    #Bắt đầu khối try-except để bắt lỗi nếu xảy ra vấn đề khi xử lý tệp.
        with open(file_path, 'r', encoding='utf-8') as file:
        #Mở tệp ở chế độ đọc ('r') với bộ mã hóa UTF-8 để đọc được tiếng Việt và các ký tự đặc biệt.
        #with đảm bảo tệp sẽ được tự động đóng sau khi hoàn tất xử lý.
        #Biến file đại diện cho tệp đang mở.
            content = file.readlines() 
            #Đọc toàn bộ các dòng trong tệp và lưu thành một danh sách các chuỗi (mỗi phần tử là một dòng, bao gồm cả ký tự xuống dòng \n).
            num_lines = len(content)  
            #Đếm số dòng bằng cách lấy độ dài của danh sách content.   
            num_chars = sum(len(line) for line in content) 
            #Đếm tổng số ký tự, bao gồm cả dấu cách và \n, bằng cách cộng độ dài của từng dòng. 
            num_words = sum(len(line.split()) for line in content) 
            #line.split() chia dòng thành danh sách các từ dựa trên khoảng trắng.
            #len(...) cho biết số từ trong mỗi dòng.
            #Dùng sum(...) để cộng tổng số từ từ tất cả các dòng.
            print(f"Số dòng: {num_lines}")
            print(f"Số ký tự: {num_chars}")
            print(f"Số từ: {num_words}")
            
    except FileNotFoundError:
    #Nếu không tìm thấy tệp,
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
        # hiển thị thông báo lỗi dễ hiểu cho người dùng.
    except Exception as e:
    #Nếu có bất kỳ lỗi nào khác, 
        print(f"Có lỗi xảy ra: {e}")
        #in ra thông báo lỗi chi tiết (e).
analyze_file('nam.txt')
#Gọi hàm analyze_file với đường dẫn 'nam.txt' để thực hiện phân tích tệp.
