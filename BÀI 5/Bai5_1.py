print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
import mymath  # Note no .py 
values = [2,4,6,8,10] 
#Khởi tạo một danh sách (list) các số chẵn từ 2 đến 10. Danh sách này sẽ được dùng để tính bình phương, lập phương và trung bình
print('Squares:') 
for v in values: 
#Vòng lặp for để duyệt qua từng phần tử v trong danh sách values
    print(mymath.square(v)) 
    #Gọi hàm square() từ mô-đun mymath để tính bình phương của giá trị v, sau đó in kết quả ra màn hình
print ('Cubes:')
#In ra dòng chữ "Cubes:" để thông báo rằng các dòng tiếp theo sẽ là kết quả lập phương của từng giá trị.
for v in values: 
#Vòng lặp for khác, cũng duyệt qua từng phần tử trong values
    print(mymath.cube(v)) 
    #Gọi hàm cube() từ mô-đun mymath để tính lập phương của từng giá trị v, sau đó in kết quả.
print('Average: ' + str(mymath.average(values)))
#Gọi hàm average() từ mô-đun mymath để tính trung bình của danh sách values,Chuyển kết quả thành chuỗi bằng str().
