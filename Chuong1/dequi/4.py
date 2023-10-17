def tinhtich(k):
    tich=1
    for i in range (1,k+1):
        tich*=i
    return tich
n=int(input())
print(tinhtich(n))
# 1 vòng lặp for có worstcase là n => O(n)