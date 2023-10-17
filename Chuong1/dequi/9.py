n = int(input())

def hanoitower(n, A, B, C):
    if n == 1:
        print(str(A) + '->' + str(C))
    else:
        hanoitower(n - 1, A, C, B)
        print(str(A) + '->' + str(C))
        hanoitower(n - 1, B, A, C)

hanoitower(n, 'A', 'B', 'C')
