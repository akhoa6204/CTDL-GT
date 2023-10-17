import time 
# n=int(input('n= '))
# bd=time.time()
# L=[]
# for i in range (2,n+1):
#     Ln=[]
#     for j in range (1,i):
#        if i%j==0:
#            Ln.append(j)
#     if sum(Ln)==i:
#         L.append(i)
# print(*L)
# kt=time.time()
# print(kt-bd)

def KTSHH(k):
    tong=0
    if k%2==0:    
        for i in range (1,k//2 +1):
            if k%i==0:tong+=i
        if tong == k : return True
        return False
n=int(input())
for i in range (1,n+1):
    if KTSHH(i):print(i,end=' ')
 
 
