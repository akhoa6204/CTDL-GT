import time 
bd=time.time()
def KTSNT(k):
    for i in range (2,int(n**0.5)+1):
        if k%i == 0:return False 
    return True
n=int(input('n= '))
for i in range (1,n+1):
    if KTSNT(i):
        print(i,end=' ')
kt=time.time()
print(kt-bd)
