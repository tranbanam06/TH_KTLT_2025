print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def is_all_digits_even(num):
#Khai báo hàm is_all_digits_even — nhận vào một số nguyên num, kiểm tra xem tất cả các chữ số của nó có phải là số chẵn không
    for digit in str(num):
    # duyệt qua từng chữ số trong một số nguyên num với digit là biến tạm của từng ký tự
        if int(digit) % 2 != 0:
        #Chuyển digit thành số nguyên rồi kiểm tra
        #Nếu không chia hết cho 2 (tức là số lẻ), thì trả về False ngay lập tức vì chỉ cần một chữ số lẻ là không đạt yêu cầu
            return False
    return True
    #Nếu vòng lặp hoàn tất mà không gặp chữ số lẻ nào, thì tất cả chữ số đều là số chẵn → trả về True
result = []
#Tạo một danh sách rỗng để lưu các số thỏa điều kiện (mọi chữ số đều chẵn)
for num in range(1000, 3001):
#Duyệt qua các số nguyên từ 1000 đến 3000 (bao gồm 3000).
    if is_all_digits_even(num):
    #Nếu num thỏa điều kiện, thì chuyển thành chuỗi và thêm vào danh sách result
        result.append(str(num))
print(",".join(result))
#join() để nối tất cả các chuỗi số trong danh sách lại thành một dòng duy nhất, cách nhau bằng dấu phẩy.
