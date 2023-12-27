def selection(n): 
    for i in range(len(n) - 1):
        min = i
        for j in range(i + 1, len(n)):
            if n[min] > n[j]:
                min = j
        n[i], n[min] = n[min], n[i]
# tựa bbule sort 
# điểm khác ở đây là 
# buble sẽ đưa phần tử lớn nhất về sau cùng
# selection sẽ lưu index của phần tử nhỏ nhất sau đó sẽ đưa nó về vị trí đầu tiên       
n = [10 , 2, 5, 6, 1, 3, 5, 4]
selection(n)
print(n)


 