def buble(n): 
    for i in range (len(n)):
        for j in range (len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

n = [1, 2, 0, 6, 5, 3, 4, -1, -2, 6, 9]
buble(n)

# i = 0 for j (0, 10) so sánh từng cặp 1 và 2 k đổi, 2 và 0 đổi thành 0 và 2 [1, 0, 2, ..] 2 và 6 k đổi tiếp tục nổi lên cuối cùng là 9
# i = 1 for j (0, 9) so sánh 1 và 0 đổi thành 0 và 1 [0, 1, 2, ...] nổi lên 6 cuối cùng[.., 6, 9]
# i = 2 for j (0, 8) so sánh như trên và nổi lên 6 
# các bước tiếp theo như trên giảm dần bước nhảy cho j 

# tựa selection
# điểm khác ở đây là 
# buble sẽ đưa phần tử lớn nhất về sau cùng
# selection sẽ lưu index của phần tử nhỏ nhất sau đó sẽ đưa nó về vị trí đầu tiên  
print("mang da sap xep\n" + str(n))
            