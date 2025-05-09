print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import datetime as dt 
#Nhập mô-đun chuẩn datetime của Python và đặt bí danh là dt để dùng cho ngắn gọn
format = '%Y-%m-%dT%H:%M:%S'
#Định nghĩa một chuỗi định dạng ngày giờ
# Ký tự 'T' để phân tách giữa ngày và giờ (đúng định dạng ISO 8601)
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format) 
#Chuyển chuỗi ngày giờ '2008-10-12T14:45:52' thành đối tượng datetime theo định dạng đã định nghĩa ở trên
print('Day ' + str(t1.day))
#In ra ngày (day) trong đối tượng t1 (kết quả sẽ là Day 12) 
print('Month ' + str(t1.month))
# In ra tháng (month) trong đối tượng t1 (kết quả sẽ là Month 10
print('Minute ' + str(t1.minute))
#  In ra phút (minute) của t1 (sẽ là Minute 45)
print('Second ' + str(t1.second)) 
# In ra giây (second) của t1 (sẽ là Second 52).
# Define todays date and time 
t2 = dt.datetime.now() 
#Lấy thời điểm hiện tại (ngày giờ hệ thống khi chạy chương trình) và lưu vào t2
diff = t2 - t1 
#Tính hiệu giữa hai đối tượng datetime (t2 - t1), kết quả là một đối tượng timedelta, đại diện cho khoảng thời gian giữa hai thời điểm
print('How many days difference? ' + str(diff.days))
# In ra số ngày chênh lệch giữa thời điểm hiện tại (t2) và thời điểm trong quá khứ (t1)
