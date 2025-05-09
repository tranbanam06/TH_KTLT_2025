print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def read_and_reverse_file(file_path):
#Định nghĩa một hàm tên là read_and_reverse_file, nhận  file_path là đường dẫn đến tệp cần đọc.
    try:
    #Bắt đầu một khối try-except để xử lý lỗi. Nếu có lỗi xảy ra trong khối try, chương trình sẽ chuyển đến phần except
        with open(file_path, 'r', encoding='utf-8') as file:
        #Mở tệp ở chế độ đọc ('r'), với mã hóa là UTF-8 để đảm bảo đọc được tiếng Việt và các ký tự đặc biệt.
        #Dùng with để tự động đóng tệp sau khi đọc xong (quản lý tài nguyên tốt).
        #file là biến đại diện cho tệp vừa mở
            content = file.readlines() 
            #Đọc toàn bộ các dòng trong tệp và lưu chúng vào danh sách content. Mỗi phần tử trong danh sách là một dòng từ tệp, bao gồm cả ký tự xuống dòng \n.
            content.reverse()
            #Đảo ngược thứ tự các dòng trong danh sách content             
            for line in content:
            #Duyệt qua từng dòng trong danh sách đã đảo ngược.
                print(line.strip()) 
                #line.strip() loại bỏ khoảng trắng và ký tự xuống dòng ở đầu/cuối dòng, rồi in ra màn hình.    
    except FileNotFoundError:
    #Nếu không tìm thấy tệp (sai đường dẫn hoặc tệp không tồn tại), in ra thông báo lỗi rõ ràng.
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
    #Nếu có bất kỳ lỗi nào khác xảy ra (ví dụ: lỗi mã hóa, quyền truy cập...), in ra thông báo lỗi và nội dung cụ thể của lỗi (e)
        print(f"Có lỗi xảy ra: {e}")
read_and_reverse_file('nam.txt')
#Gọi hàm read_and_reverse_file với đường dẫn 'bài 7/nam.txt' để thực thi đoạn mã.
