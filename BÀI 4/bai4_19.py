print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")
def sieve_of_eratosthenes(limit):
#Định nghĩa một hàm có tên là sieve_of_eratosthenes
#Nhận vào một số limit → giới hạn trên, tìm các số nguyên tố nhỏ hơn hoặc bằng limit
    primes = [True] * (limit + 1)
    #Tạo một danh sách primes gồm limit + 1 phần tử, tất cả đều là True
    #Ý nghĩa: giả sử ban đầu tất cả các số là nguyên tố.
    primes[0] = primes[1] = False 
    #Đặt 0 và 1 là không phải số nguyên tố. 
    for i in range(2, int(limit**0.5) + 1):
    #Duyệt các số từ 2 đến căn của limit(Vì nếu một số không nguyên tố thì nó sẽ có ít nhất một ước ≤ √n)
        if primes[i]:
        #Nếu i vẫn còn được đánh dấu là True → tức là i là số nguyên tố
            for j in range(i * i, limit + 1, i):
            #Bắt đầu từ i² bước i (vì các bội nhỏ hơn i² đã bị loại bởi các số nhỏ hơn trước đó
                primes[j] = False
                #Đánh dấu j không phải là số nguyên tố
    prime_numbers = tuple(i for i in range(limit + 1) if primes[i])
    #Tạo một tuple chứa các chỉ số i mà primes[i] == True → tức là số nguyên tố.
    return prime_numbers
    #Trả về danh sách các số nguyên tố dưới dạng tuple
P = sieve_of_eratosthenes(10**6)
#Gọi hàm sàng với giới hạn 1 triệu
print(P[:20])
#In ra 20 số nguyên tố đầu tiên trong danh sách P
print(f"Có {len(P)} số số nguyên tố nhỏ hơn 1 triệu ")
