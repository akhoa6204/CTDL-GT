def tinhtong(k):
    tong=0
    for i in range(0,k+1):
        tong+=i
    return tong
n=int(input())
print(tinhtong(n))
# 1 vòng lặp for có worstcase là n => O(n)
