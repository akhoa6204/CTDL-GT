# liệt kê xâu nhị phân / chỉnh hợp lặp
# def find(i,k,n,x):
#     for j in range(0,n):
#         x[i]=j
#         if i ==k-1:
#             print(x)
#         else: 
#             find(i+1,k,n,x)
#     # x[0]=0
#     # đệ qui 1 x[1]=0 
#     # đệ qui 2 x[2]=0 (th neo) => in x =[0,0,0]
#     # quay lại đệ qui 1 xét tiếp giá trị còn lại của x2 =1 
#     # => in x =[0,0,1]
#     # quay lại đệ qui 1 xét th x[1]=1 lặp lại các bước thứ x[2]
#     # tương tự với x[0]
# def find5(i,k,n,x):
#     for j in range (1,n+1):
#         x[i]=j
#         if i==k-1:
#             print(x)
#         else : find5(i+1,k,n,x)
# x=[0]*3
# find(0,3,2,x)
# find5(0,3,5,x)
# # không lặp 
def Try(i,n,k,A,S):
    for j in range (0,n):
        if A[j] ==1:
            S[i]=j
            A[j]=0
            if i ==k-1:
                print(S)
            else : 
                Try(i+1,n,k,A,S)
            A[j]=1
n=4
k=3
A=[1]*n
S=[0]*k
Try(0,n,k,A,S)
# 1

# n=int(input())
# i=1
# while i<=n:    
#     for j in range (1,6,2):
#         if i<=n:
#             print(i,end=' ')
#             i+=j
    
# 2
# def chl(i,n,k,A):
#     for j in range (0,n):
#         A[i]=j
#         if i ==k-1 :
#             print(*A)
#         else : chl(i+1,n,k,A)
# A=[0]*3
# chl(0,3,3,A)

def IN(x):
    if x ==2 :
        print (x)
    else : 
        for i in range (2,int(x**0.5)+1):
            if x%i==0 : break
        else : 
            print(x)
        IN(x-1)  
def INX(x):
    for i in  range (2,int(x**0.5)+1):
        if i%2!=0:     
            for j in range (2,i):
                if i%j==0 : break
            else : print(i,end=' ')
n=int(input())
IN(n)
INX(n)
