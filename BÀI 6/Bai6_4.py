print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
class RomanToInteger:#Tạo một lớp (class) tên là RomanToInteger, dùng để chứa các hàm chuyển đổi từ số La Mã sang số nguyên.
    def __init__(self):#Đây là hàm khởi tạo (__init__), được chạy tự động khi tạo đối tượng từ lớp này.
        self.roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        #Đây là một từ điển (dictionary) chứa các ký hiệu La Mã làm khóa (key) và giá trị số tương ứng làm giá trị (value).
    def roman_to_int(self, roman):#Đây là hàm dùng để chuyển chuỗi La Mã thành số nguyên.
        total = 0 #Biến total dùng để lưu tổng kết quả sau khi xử lý. 
        prev_value = 0 #Biến prev_value lưu giá trị La Mã trước đó (khi duyệt từ phải sang trái), giúp kiểm tra khi nào cần cộng, khi nào cần trừ. 
        for char in reversed(roman):
        #Duyệt từng ký tự trong chuỗi La Mã từ phải sang trái.(Vì trong quy tắc La Mã, nếu chữ nhỏ hơn đứng trước chữ lớn hơn thì phải trừ)
            current_value = self.roman_map[char] #Lấy giá trị số của ký tự La Mã hiện tại từ từ điển roman_map
            if current_value < prev_value:#Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, thì trừ (vì nó đang ở dạng như IV = 5 - 1 = 4).
                total -= current_value
            else:#Ngược lại, nếu lớn hơn hoặc bằng, thì cộng giá trị vào tổng.
                total += current_value
            prev_value = current_value#Cập nhật prev_value để so sánh với ký tự tiếp theo (bên trái).
        return total# Trả về kết quả cuối cùng — số nguyên tương ứng với số La Mã đã nhập.
if __name__ == "__main__":#Đây là cách kiểm tra nếu bạn đang chạy chương trình trực tiếp (chứ không phải import từ file khác).
    roman_converter = RomanToInteger()#Tạo một đối tượng từ lớp RomanToInteger, gọi là roman_converter.
    roman_number = input("Nhập số La Mã: ").upper()# Hiển thị thông báo cho người dùng nhập số La Mã.Và dùng Hàm .upper() chuyển chữ thường thành chữ in hoa để xử lý đúng.
    result = roman_converter.roman_to_int(roman_number)#Gọi hàm roman_to_int() để chuyển đổi chuỗi La Mã sang số nguyên và lưu kết quả vào biến result.
    print(f"Số nguyên tương ứng là: {result}")
