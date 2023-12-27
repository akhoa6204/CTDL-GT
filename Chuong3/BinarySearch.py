# dãy đã sắp xếp 
def Binary(n, a) :
    low = 0 
    high = len(n) - 1 
    mid = (high + low) // 2
    mid_value = n[mid]
    while low <= high :
        mid = (high + low) // 2
        mid_value = n[mid] 
        if mid_value == a: 
            return mid
        elif mid_value < a: 
            low = mid + 1
        else: 
            high = mid - 1
    return -1

n = [1, 2, 5, 9, 11, 77, 87, 98, 99]
a = 77
result = Binary(n, a) 
if result != -1:
    print(f"Giá trị {a} được tìm thấy tại vị trí {result}")
else:
    print(f"Giá trị {a} không tìm thấy vị trí")  
        