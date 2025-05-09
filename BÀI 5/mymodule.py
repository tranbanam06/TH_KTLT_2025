# mymodule.py
def find_max(lst):
#Định nghĩa một hàm có tên là find_max, nhận một tham số đầu vào là lst – danh sách các giá trị.
    return max(lst)
    #Sử dụng hàm dựng sẵn max() để tìm giá trị lớn nhất trong danh sách lst và trả về giá trị đó
def find_min(lst):
#Định nghĩa một hàm có tên là find_min, nhận một tham số đầu vào là lst – danh sách các giá trị
    return min(lst)
    ##Sử dụng hàm dựng sẵn min() để tìm giá trị nhỏ nhất trong danh sách lst và trả về giá trị đó
def sort_list(lst):
#Định nghĩa một hàm có tên là sort_list, nhận một tham số đầu vào là lst – danh sách các giá trị  
    return sorted(lst)
    #sorted(lst) là hàm dựng sẵn trong Python, trả về một bản sao của danh sách lst được sắp xếp theo thứ tự tăng dần,Không làm thay đổi danh sách gốc lst
def find_max_index(lst):
#Định nghĩa một hàm có tên là find_max_index, nhận một tham số đầu vào là lst – danh sách các giá trị 
    return lst.index(max(lst))
    #max(lst): tìm giá trị lớn nhất trong danh sách
    #lst.index(...): tìm vị trí (index) của giá trị đó trong danh sách.
def find_min_index(lst):
#Định nghĩa một hàm có tên là find_min_index, nhận một tham số đầu vào là lst – danh sách các giá trị 
    return lst.index(min(lst))
    #min(lst): tìm giá trị nhỏ nhất trong danh sách
    #lst.index(...): tìm vị trí (index) của giá trị đó trong danh sách.
