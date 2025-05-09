print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

from sort_module import bubbleSort
#Import hàm bubbleSort từ module sort_module.py
n = int(input("Nhập số lượng phần tử trong danh sách: "))
#Nhập vào số lượng phần tử n mà người dùng muốn đưa vào danh sách từ bàn phím và chuyển nó sang dạng số nguyên.
nlist = []
#Tạo một danh sách rỗng để lưu các phần tử người dùng nhập.
for i in range(n):
#Lặp i từ 0 đến n-1,vòng lặp chạy đúng n lần, tương ứng với số lượng phần tử mà người dùng muốn nhập
  value = float(input(f"Nhập phần tử thứ {i+1}: "))
  #Hiển thị lời nhắc: "Nhập phần tử thứ 1:", "Nhập phần tử thứ 2:", v.v.
  #Dùng float() để chuyển đầu vào từ chuỗi thành số thực (float).
  #Dùng f-string để chèn giá trị i+1 vào thông báo, giúp hiển thị thứ tự rõ ràng hơn cho người dùng
  nlist.append(value)
  #Thêm giá trị vừa nhập vào danh sách nlist
sorted_list = bubbleSort(nlist)
#Gọi hàm bubbleSort() để sắp xếp danh sách nlist.
print("Danh sách sau khi sắp xếp:", sorted_list)
