def SNT(k):
    if k==2 :
        print(k) 
    else :
        for i in range (2,int(k**0.5)+1):
            if k%i==0:
                break
        else :
            print(k)
        SNT(k-1)
n=int(input())
SNT(n)
# 1 vòng lặp for có worstcase là (n**0.5)-1
# đệ qui có worstcase là n 
# => O(n^1.5)
