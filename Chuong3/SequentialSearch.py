def sequential(n, a):
    for i in range(len(n)):
        if n[i] == a:
            return i
    return -1
n = [64, 34, 25, 12, 22, 11, 90]
a = 22
result = sequential(n, a)
if result != -1:
    print(f"Phần tử {a} được tìm thấy tại vị trí {result}.")
else:
    print(f"Phần tử {a} không có trong mảng.")
