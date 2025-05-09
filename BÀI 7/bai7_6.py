print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import os
#Nhập mô-đun os, dùng để làm việc với hệ thống tệp (ở đây là lấy kích thước tệp với os.stat).
def file_read_from_tail(fname, lines):
#Định nghĩa hàm file_read_from_tail, nhận vào:
#fname: tên (hoặc đường dẫn) của tệp.
#lines: số dòng cuối muốn đọc.
    bufsize = 8192
    #Kích thước mỗi lần đọc (buffer) là 8192 byte (8 KB).
    fsize = os.stat(fname).st_size
    #Lấy kích thước tệp (tính bằng byte).
    iter = 0 #iter để theo dõi số lần đọc.
    data = [] #data là danh sách chứa các dòng đã đọc.
    with open(fname) as f:
    #Mở tệp ở chế độ mặc định ('r', đọc văn bản).
        if bufsize > fsize:
        #Nếu tệp nhỏ hơn kích thước mỗi lần đọc, thì giảm bufsize cho phù hợp để tránh đọc vượt quá kích thước tệp.
            bufsize = fsize           
        while True:
        #Mỗi vòng lặp, con trỏ tệp sẽ dịch ngược về phía đầu tệp theo bội số của bufsize.
            iter += 1 #Tăng số lần lặp. Mỗi lần lặp tương ứng với việc đọc lùi thêm một bufsize (mặc định 8192 byte).
            f.seek(fsize - bufsize * iter)#Di chuyển con trỏ đọc (file pointer) đến vị trí cách cuối tệp bufsize * iter byte.
            data.extend(f.readlines())#Đọc tất cả các dòng kể từ vị trí đó đến hết tệp và thêm vào danh sách data.
            if len(data) >= lines or f.tell() == 0:
            #Nếu đã đọc đủ số dòng yêu cầu (lines), hoặc đã chạm đến đầu tệp (f.tell() == 0), thì:
                print(''.join(data[-lines:]))
                #data[-lines:]Lấy số dòng cuối cùng từ danh sách data.
                #''.join(...)Nối tất cả các dòng lại thành một chuỗi lớn (giữ nguyên định dạng dòng, vì các dòng trong data vẫn có \n ở cuối).
                #print(...)In ra màn hình các dòng cuối cùng đã nối.
                break#Thoát khỏi vòng lặp while True sau khi đã đủ số dòng yêu cầu hoặc đã đến đầu tệp.
file_read_from_tail('nam.txt', 2)
#Gọi hàm để đọc 2 dòng cuối cùng của tệp 'nam.txt'.
