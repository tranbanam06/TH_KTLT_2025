print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
"""hàm tính tham số hàm này nhận 3 tham số t: lãi suất mỗi tháng (theo phần trăm),n: số vốn ban đầu,
k: số tháng gửi tiết kiệm"""
def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    total_amount = n * ((1 + t / 100) ** k)
    return total_amount

# Nhập lãi suất, số vốn và số tháng
t = float(input("Nhập lãi suất tiết kiệm (t%/tháng): "))#Nhập lãi suất (t): số thực
n = float(input("Nhập số vốn ban đầu (n): "))#Nhập số vốn ban đầu (n): số thực
k = int(input("Nhập số tháng gửi (k): "))#Nhập số tháng gửi (k): số nguyên

result = benefit(t, n, k)#Gọi hàm benefit(t, n, k) để tính tổng tiền nhận được.
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}") #In kết quả với 2 chữ số thập phân (dùng :.2f để làm tròn)


