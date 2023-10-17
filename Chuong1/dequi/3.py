def tinhtich(k):
    if k==1:
        return 1
    else :
        return k * tinhtich(k-1)
n=int(input())
print(tinhtich(n)) 
# đệ qui có worstcase là n => O(n)