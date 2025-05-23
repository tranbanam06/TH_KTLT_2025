print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import math #Import thư viện toán học math để sử dụng các hàm như sqrt (căn bậc hai), dùng để tính khoảng cách
pos = [0,0] 
#Biến pos là một danh sách gồm 2 phần tử đại diện cho tọa độ (x, y)
#Ban đầu, vị trí là [0, 0] tức là điểm gốc
while True: #Vòng lặp vô hạn, sẽ chạy cho đến khi bạn nhập một chuỗi rỗng ("") để kết thúc
 s = input("Vui lòng nhập lệnh di chuyển: ") #Yêu cầu người dùng nhập lệnh di chuyển
 if not s: #Nếu chuỗi s rỗng (người dùng chỉ nhấn Enter), chương trình sẽ thoát khỏi vòng lặp
  break 
 movement = s.split(" ") #Tách chuỗi s thành 2 phần: hướng (direction) và số bước (steps)
 direction = movement[0] #Lấy phần đầu tiên làm hướng di chuyển
 steps = int(movement[1]) #Lấy phần thứ hai làm số bước di chuyển, và ép kiểu về int
 if direction=="UP": 
  pos[0]+=steps 
 elif direction=="DOWN": 
  pos[0]-=steps 
 elif direction=="LEFT": 
  pos[1]-=steps
 elif direction=="RIGHT": 
  pos[1]+=steps 
 else: #Nếu hướng nhập không đúng, thì bỏ qua không làm gì
  pass 
###################### 
print ("Khoagr cách từ hiện tại vị trí đầu tiên là: ",int(round(math.sqrt(pos[1]**2+pos[0]**2))))
#math.sqrt(pos[0]**2 + pos[1]**2): Đây là công thức Pythagoras để tính khoảng cách từ gốc tọa độ (0,0) đến vị trí (x, y)
#round(...) làm tròn số thực.
#int(...) chuyển kết quả thành số nguyên (loại bỏ phần thập phân sau khi làm tròn).

