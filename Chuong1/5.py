n=int(input('n= '))
L=[]
for i in range (2,n+1):
    Ln=[]
    for j in range (1,i):
       if i%j==0:
           Ln.append(j)
    if sum(Ln)==i:
        L.append(i)
print(*L)