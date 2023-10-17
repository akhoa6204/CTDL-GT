def giaithua(n):
    if n==1:
        return 1 
    else : return n*giaithua(n-1)
n=int(input("n= "))
k=int(input("k= "))
print('To hop =',giaithua(n)/(giaithua(n-k)*giaithua(k)))
print('Chinh hop =',giaithua(n)/giaithua(n-k))
print('Hoan vi =',giaithua(n))