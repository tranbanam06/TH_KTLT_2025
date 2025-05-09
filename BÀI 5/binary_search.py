
# binary_search.py
def binary_search(sorted_list, value):
    """
    Hàm tìm kiếm nhị phân (Binary Search) trên danh sách đã sắp xếp.
    Trả về True nếu tìm thấy phần tử 'value', False nếu không tìm thấy.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Tính chỉ số giữa
        if sorted_list[mid] == value:
            return True  # Nếu tìm thấy phần tử
        elif sorted_list[mid] < value:
            low = mid + 1  # Nếu giá trị ở giữa nhỏ hơn value, tìm kiếm ở nửa phải
        else:
            high = mid - 1  # Nếu giá trị ở giữa lớn hơn value, tìm kiếm ở nửa trái
    
    return False  # Nếu không tìm thấy phần tử
