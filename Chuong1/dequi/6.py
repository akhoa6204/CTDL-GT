def SNT(k):
    for i in range (2, k+1):
        for j in range (2,int(i**0.5+1)):
            if i%j==0:
                break
        else :
            print(i)
n=int(input())
SNT(n)
# 1 vòng lặp for có worstcase là (n**0.5)-1
# 1 vòng lặp for có worstcase là n 
# => O(n^1.5)