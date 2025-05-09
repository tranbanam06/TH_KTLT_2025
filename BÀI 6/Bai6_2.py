print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

class Hinhchunhat(object): 
   #Đây là dòng tạo ra một lớp (class) tên là Hinhchunhat, dùng để mô tả hình hinhchunhat.
   #(object) có nghĩa là lớp này kế thừa từ lớp gốc trong Python (có thể hiểu là "mọi lớp đều bắt nguồn từ object")
   def __init__(self, dai, rong):
   #Đây là cách khai báo một hàm đặc biệt tên là __init__
   # Hàm này được Python gọi tự động khi bạn tạo một đối tượng mới từ lớp đó.
   # self: đại diện cho chính đối tượng đang được tạo (luôn phải có trong phương thức của lớp).
   # dai, rong: là hai tham số đầu vào, bạn truyền vào khi tạo đối tượng — ví dụ như chiều dài và chiều rộng. 
      self.dai = dai
      #self.dai = dai nghĩa là gán giá trị chiều dài cho thuộc tính dai của đối tượng.
      self.rong = rong
      #self.rong = rong nghĩa là gán giá trị chiều rộng cho thuộc tính rộng của đối tượng.
############################### 
   def area(self):
   ##Khai báo một hàm tên là area dùng để tính shinhchunhat
      return self.dai * self.rong
aHinhchunhat= Hinhchunhat(4, 5) 
print (aHinhchunhat.area())
