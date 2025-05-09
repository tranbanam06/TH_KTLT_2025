print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

class StringReverser:
# Tạo một lớp (class) có tên là StringReverser.Lớp này dùng để xử lý việc đảo ngược thứ tự các từ trong một chuỗi văn bản.
    def __init__(self, input_string):
    # Đây là hàm khởi tạo (__init__) của lớp:Khi tạo một đối tượng từ lớp này, bạn truyền vào một chuỗi (ví dụ: "hello .py").
        self.input_string = input_string 
        #self.input_string = input_string sẽ lưu trữ chuỗi đó vào thuộc tính input_string của đối tượng.
    def reverse_words(self):
    #Đây là một phương thức (hàm bên trong lớp), có nhiệm vụ đảo ngược thứ tự các từ trong chuỗi.
        words = self.input_string.split()
        #self.input_string: Đây là chuỗi bạn đã nhập vào trước đó và được lưu trong đối tượng của lớp StringReverser. Ví dụ: "hello .py".
        #.split(): Hàm split() trong Python dùng để tách chuỗi thành các phần (thường là các từ) dựa trên một ký tự phân cách. Mặc định, split() sử dụng dấu cách (" ") làm ký tự phân cách.
        reversed_words = words[::-1]
        #Dòng này dùng cú pháp [::-1] để đảo ngược danh sách các từ. 
        return ' '.join(reversed_words)
        #Hàm ' '.join(...) sẽ nối danh sách từ lại thành một chuỗi, ngăn cách bằng dấu cách.  
if __name__ == "__main__":
#Dòng này đảm bảo rằng đoạn code bên dưới chỉ chạy khi bạn chạy file trực tiếp, không bị chạy khi file được import vào chỗ khác.
    input_string = 'hello .py'
    # Gán chuỗi "hello .py" vào biến input_string.
    reverser = StringReverser(input_string)
    #Tạo một đối tượng reverser từ lớp StringReverser, truyền chuỗi vào để lưu trữ.
    result = reverser.reverse_words()
    # Gọi hàm reverse_words() để đảo ngược các từ trong chuỗi.
    print(f"Dữ liệu vào: {input_string}")
    print(f"Đầu ra: {result}")
