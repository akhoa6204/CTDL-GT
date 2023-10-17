n=int(input('n= '))
L=[]
for i in range(0,n):
   L.append(float(input()))
max=L[0]
for i in range(len(L)):
    if L[i] > max:
        max=L[i]
print('Số lớn nhất là',max) 
    