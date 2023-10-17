def F(k):
    if (k<=2):
        return 1
    else:
        return F(k-1)+F(k-2)
n=int(input())
print(F(n))
# 1 vòng lặp for có worstcase là n => O(n)