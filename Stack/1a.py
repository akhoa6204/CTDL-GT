#1.	Định nghĩa các phép toán cho stack và sử dụng nó để chuyển cơ số từ cơ số 10, sang cơ số y
class Stack: 
    def __init__(self):
        self.list=[]
        self.size=0
    def Push(self,x):
            self.list.append(x)
            self.size+=1
    def Popt(self):
        if self.size>0:
            self.size-=1
            return self.list.pop()
    def GetTop(self):
        if self.size>0:
            return self.list[self.size-1]
    def isEmpty(self):
        if self.size>0  : return False 
        else: return True
example = Stack() 
thuong=int(input('Số cơ số 10 muốn chuyển đổi cơ số: '))
i=int(input('cơ số muốn chuyển đổi: '))
while thuong!=0:
    sodu=thuong%i
    thuong=thuong//i
    example.Push(sodu)
kq=''
while example.isEmpty() is False:
    kq=kq+str(example.Popt())
print('Kết quả sau khi chuyển đổi: ',end='')
print(kq,end='')