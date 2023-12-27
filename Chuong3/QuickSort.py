def quick(n): 
    if len(n) < 2: 
        return n
    else :
        a = n[0]
        middle = [x for x in n if x == a]
        left = [x for x in n if x < a]
        right = [x for x in n if x > a]
        return quick(left) + middle + quick(right)
    
n = [1, 2, 5, 4, 5, 3, 1, 5, 9, 10, 11, 78 , -12]
print(quick(n))

# chia nhỏ list thành 3 phần | left là mảng < a | right là mảng > a | middle là mảng = a
# sau đó tiếp tục đệ qui left và right cho đến khi len(left), len(right) < 2