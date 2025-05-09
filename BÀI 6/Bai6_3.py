print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

class Nguoi(object):#Tạo lớp Nguoi (nghĩa là “Người”), là lớp cha (lớp cơ sở).
    def getGender(self):#Đây là một phương thức (hàm bên trong lớp) tên là getGender
        return "Unknown"#Phương thức này trả về chuỗi "Unknown" vì chưa biết là nam hay nữ.
class Nam(Nguoi):
#Đây là lớp con tên là Nam, kế thừa từ lớp Nguoi
    def getGender(self):
    #Phương thức getGender trong lớp Nam ghi đè (override) phương thức trong lớp Nguoi
        return("Nam")
    #Tức là: nếu gọi getGender() từ đối tượng thuộc lớp Nam, sẽ trả về "Nam"
class Nu(Nguoi):
#Đây là lớp con tên là Nu, kế thừa từ lớp Nguoi
    def getGender(self):
    #Phương thức getGender trong lớp Nu ghi đè (override) phương thức trong lớp Nguoi
        return "Nữ"
        #Tức là: nếu gọi getGender() từ đối tượng thuộc lớp Nu, sẽ trả về "Nữ"
aNam = Nam()
#aNam là một đối tượng thuộc lớp Nam
aNu = Nu()
#aNu là một đối tượng thuộc lớp Nu.
print(aNam.getGender())
print(aNu.getGender())
