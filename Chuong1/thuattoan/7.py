n=int(input())
def gt_kDQ(n):   
    tich=1
    for i in range(1,n+1):
        tich*=i
    return tich
print(str(n)+'!=',gt_kDQ(n)) 
def gtDQ(n):
    if n==0:
        return 1
    return n*gtDQ(n-1)
print(str(n)+'!=',gtDQ(n))
    
