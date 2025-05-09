print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
day_tu = input('Nhập cac day tu: ').split()
#input(...): yêu cầu người dùng nhập một dòng văn bản.
#.split(): tách dòng thành các từ, dựa trên khoảng trắng.
max_length = max(len(tu) for tu in day_tu)
#Duyệt từng từ tu trong day_tu và tính len(tu) (độ dài từ).
#Dùng max(...) để tìm độ dài lớn nhất.
tu_dai_nhat = [tu for tu in day_tu if len(tu) == max_length]
#Tạo một danh sách các từ có độ dài bằng max_length
print('Tu dai nhat:', ' '.join(tu_dai_nhat))
#' '.join(...) để nối các từ dài nhất lại thành chuỗi