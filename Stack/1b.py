# Danh sách liên kết 
class node : 
    def __init__(self,da_ta) : 
        self.data=da_ta
        self.next=None 
class Stack: 
    def __init__(self) : 
        self.head = None
        self.last=None 
    def push(self,x): 
        x =node(x)
        if self.head is None:
            self.head = x 
            self.last = x 
        else : 
            self.last.next = x 
            self.last = x
    def pop(self):
        if self.head is None: 
            return None
        else:
            cur= self.head
            pre_cur = None 
            while cur.next is not None: 
                pre_cur = cur
                cur=cur.next
            if pre_cur is None: 
                self.head=None
                self.last=None
            else: 
                pre_cur.next = None
                self.last=pre_cur 
            return cur.data 
    def get_top(self):  
        if self.last is not None:
            return self.last.data 
        return None 
    def isEmpty(self):
        if self.head is None: return True 
        else : return False 
example = Stack() 
thuong=int(input('Số cơ số 10 muốn chuyển đổi cơ số: '))
i=int(input('cơ số muốn chuyển đổi: '))
while thuong!=0:
    sodu=thuong%i
    thuong=thuong//i
    example.push(sodu)

kq=''
while example.isEmpty() is False:
    kq=kq+str(example.pop())
print('Kết quả sau khi chuyển đổi: ',end='')
print(kq,end='')

            
