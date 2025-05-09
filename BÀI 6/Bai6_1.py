print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
class Circle(object): 
   #Đây là dòng tạo ra một lớp (class) tên là Circle, dùng để mô tả hình tròn.
   #(object) có nghĩa là lớp này kế thừa từ lớp gốc trong Python (có thể hiểu là "mọi lớp đều bắt nguồn từ object").
   def __init__(self, r): 
   #Đây là hàm khởi tạo, tự chạy khi tạo một đối tượng (ví dụ như Circle(2)).
      self.radius = r 
      #self là cách để đối tượng truy cập vào chính nó.
      #r là bán kính bạn đưa vào khi tạo hình tròn.
      #self.radius = r có nghĩa là "lưu lại giá trị bán kính vào đối tượng".
   def area(self): 
   #Khai báo một hàm tên là area dùng để tính shinhtron, nhận vào một tham số R là bán kính hình tròn
      return self.radius**2*3.14 
aCircle = Circle(2) 
#Dòng này tạo một đối tượng tên là aCircle, đại diện cho một hình tròn có bán kính là 2.
print (aCircle.area())
