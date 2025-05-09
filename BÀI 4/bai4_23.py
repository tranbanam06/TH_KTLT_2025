print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def count_letters_and_digits(sentence):
#Định nghĩa một hàm tên count_letters_and_digits, nhận đầu vào là một chuỗi sentence
     letters_count = sum(c.isalpha() for c in sentence)
     #for c in sentence: Duyệt từng ký tự c trong câu
     #c.isalpha(): Trả về True nếu c là chữ cái (a–z, A–Z)
     #sum(...): Cộng tất cả giá trị True (vì trong Python, True = 1, False = 0) → ra tổng số chữ cái
     digits_count = sum(c.isdigit() for c in sentence)
     #for c in sentence: Duyệt từng ký tự c trong câu
     #c.isdigit(): Trả về True nếu c là chữ số (0–9).
     #sum(...): Tính tổng tất cả ký tự là số
     return letters_count, digits_count
     #Trả về hai kết quả: tổng số chữ cái và tổng số chữ số.
input_sentence = input("Nhâp câu: ")
letters, digits = count_letters_and_digits(input_sentence) 
#Gọi hàm count_letters_and_digits với câu vừa nhập
print(f"số chữ cái là: {letters}")
print(f"số chữ số là: {digits}")
