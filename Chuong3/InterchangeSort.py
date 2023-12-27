def interchange(n):
    for i in range(0, len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] > n[j] : 
                n[i], n[j] = n[j], n[i]
n = [5, 3, 2, 4, 6, 8, 1, 11, 9]
interchange(n)
print(*n)

# đổi chỗ trực tiếp 
# so sánh 5 và 3 đổi thành 3, 5 tiếp tục so 3 và 2 đổi thành 2, 5 ,3, ... 
# hết vòng lặp 1: 1, 5, 3, 4 , 6, 8, 2, 11, 9
# tiếp tục cho đến khi hết vòng lặp     