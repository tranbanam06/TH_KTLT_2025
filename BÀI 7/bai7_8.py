print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def write_list_to_file(fname, data_list):
#Định nghĩa một hàm tên là write_list_to_file, nhận vào:
#fname: tên hoặc đường dẫn đến tệp đích.
#data_list: danh sách dữ liệu cần ghi.
    with open(fname, 'w') as file:
    #Mở tệp ở chế độ ghi đè ('w' – write mode). Nếu tệp đã tồn tại, nội dung cũ sẽ bị xóa.
    #Biến file đại diện cho tệp đang mở.
    #Câu lệnh with giúp tự động đóng tệp sau khi đọc xong, tránh rò rỉ tài nguyên.
        for item in data_list:
        #Duyệt qua từng phần tử trong danh sách data_list.
            file.write(f"{item}\n") 
            #Ghi mỗi phần tử vào tệp, kết thúc bằng ký tự xuống dòng (\n) để mỗi phần tử hiển thị trên một dòng riêng biệt.
my_list = ["Python", "Java", "C++", "JavaScript", "Ruby"]
#Danh sách mẫu gồm tên các ngôn ngữ lập trình.
file_name = 'output.txt'
#Đường dẫn tệp đích để ghi nội dung danh sách vào.
write_list_to_file(file_name, my_list)
#Gọi hàm write_list_to_file để thực hiện ghi danh sách vào tệp output.txt.
print(f"Nội dung của danh sách đã được ghi vào tệp '{file_name}'.")
#In thông báo xác nhận khi ghi tệp hoàn tất.
