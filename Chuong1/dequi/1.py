def tong(k):
    if k==0:
        return 0
    else : 
        return k + tong(k-1)
n=int(input())
print(tong(n))
# đệ qui với worstcase là n lần => O(n)