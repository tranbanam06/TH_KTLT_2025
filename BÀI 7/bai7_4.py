print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def read_first_n_lines(file_path, n):
#Định nghĩa một hàm có tên là read_first_n_lines, nhận vào:
#file_path: đường dẫn đến tệp cần đọc.
#n: số dòng đầu tiên muốn đọc từ tệp.
    try:
    #Bắt đầu một khối try-except để xử lý các lỗi có thể xảy ra trong quá trình mở hoặc đọc tệp.
        with open(file_path, 'r', encoding='utf-8') as file:
        #Mở tệp ở chế độ đọc ('r'), sử dụng mã hóa UTF-8 để đảm bảo đọc được tiếng Việt và ký tự đặc biệt.
        #Câu lệnh with giúp tự động đóng tệp sau khi đọc xong, tránh rò rỉ tài nguyên.
        #Biến file đại diện cho tệp đang mở.
            for i in range(n):
            #Lặp từ 0 đến n-1, tức là thực hiện việc đọc n dòng.
                line = file.readline()  
                #Đọc một dòng duy nhất từ tệp tại mỗi vòng lặp. Trả về chuỗi bao gồm ký tự \n nếu dòng chưa phải là dòng cuối.
                if not line:
                #Kiểm tra nếu dòng là rỗng (line == ''), tức là đã đến cuối tệp, thì thoát khỏi vòng lặp (dù chưa đủ n dòng).            
                    break
                print(line.strip()) 
                #In dòng vừa đọc ra màn hình, sau khi loại bỏ ký tự khoảng trắng đầu/cuối dòng, bao gồm cả \n.     
    except FileNotFoundError:
    #Nếu tệp không tồn tại tại đường dẫn đã cho, in ra thông báo lỗi rõ ràng.
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
    #Nếu có lỗi khác (như lỗi mã hóa, quyền truy cập...), in ra thông báo cùng thông tin chi tiết từ biến e.
        print(f"Có lỗi xảy ra: {e}")
read_first_n_lines('nam.txt', 1)
#Gọi hàm và yêu cầu đọc 1 dòng đầu tiên của tệp 'nam.txt'.
