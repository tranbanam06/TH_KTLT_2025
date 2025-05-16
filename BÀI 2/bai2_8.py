a, b = 1, 2
total  =  0 #Dùng để lưu tổng các số chẵn trong dãy Fibonacci
print(a,end =" ") # In số đầu tiên a (là 1), không xuống dòng
while (a <= 4000000-1):
    if a % 2 == 0:
        total += a ##Nếu a là số chẵn, thì cộng vào total.
    a , b = b, a + b
    print (a,end=" ")
print("\nSum of even-valued terms in Fibonacci series: ", total)
#In tổng các số chẵn trong dãy Fibonacci nhỏ hơn 4 triệu.
print ("Sinh Viên: Tran Ba Nam")
print ("MSV: 235752020710046")