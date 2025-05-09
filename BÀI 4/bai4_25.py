print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
input_str = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")
#Lệnh input() yêu cầu người dùng nhập một chuỗi từ bàn phím
numbers = [int(x) for x in input_str.split(",")]
#input_str.split(","): Chia chuỗi input_str thành một danh sách các chuỗi con, tách nhau bởi dấu phẩy
#[int(x) for x in ...]:, lặp qua mỗi phần tử x trong danh sách chuỗi và chuyển mỗi phần tử thành một số nguyên bằng cách sử dụng hàm int(x)
odd_numbers = [num for num in numbers if num % 2 != 0]
#num for num in numbers: Duyệt qua từng số trong danh sách numbers
#if num % 2 != 0: Chỉ chọn các số mà số đó chia cho 2 không dư 0 (tức là các số lẻ)
print("Các số lẻ là:", ",".join(map(str, odd_numbers)))
#map(str, odd_numbers): Chuyển mỗi phần tử trong danh sách odd_numbers (các số lẻ) thành chuỗi.
#",".join(...): Dùng để nối các phần tử của danh sách (sau khi đã chuyển sang chuỗi) bằng dấu phẩy.