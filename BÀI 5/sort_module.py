def bubbleSort(arr):
#Định nghĩa hàm bubbleSort nhận vào một danh sách arr và trả về danh sách đã sắp xếp
    n = len(arr)
    #Xác định độ dài của danh sách — số phần tử cần sắp xếp.
    for i in range(n):
        #Vòng lặp ngoài chạy n lần (từ 0 đến n-1) — mỗi lần đảm bảo một phần tử lớn "nổi" lên đúng vị trí.
        for j in range(0, n-i-1):
        #Phạm vi n - i - 1 vì sau mỗi vòng lặp ngoài, phần tử lớn nhất đã ở cuối, nên không cần kiểm tra lại
            if arr[j] > arr[j+1]:
            #Nếu phần tử trước lớn hơn phần tử sau → hoán đổi.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
