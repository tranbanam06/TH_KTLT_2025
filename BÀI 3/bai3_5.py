a="Hello Guy!" #gán biến toàn cục a bằng xâu hello guy
def say():# khai báo hàm say
    global a #chuyển biến a từ cục bộ lên toàn cục
    a="Vinh University" # gán biến cụ bộ a bằng xâu Vinh University
    print(a)
say() #gọi hàm say với biến cục bộ(biến toàn cục mới)
print(a) # in ra màn hình với a là biến toàn cụ mới, biến toàn cục mới là biến cụ bộ
print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
"""Giải thích: mặc dù đã khai báo biến toàn cục là Hello Guy
nhưng khi khai bái hàm dùng 
lệnh global đã làm thay đổi biến cục bộ là Vinh University
thành biến toàn cục thay cho Hello Guy"""
