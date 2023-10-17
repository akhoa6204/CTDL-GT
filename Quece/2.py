#2.Viết chương trình sinh ra n số tự nhiên một cách ngẫu nhiên, sử dụng queue để chứa dãy số đó. Sau đó lấy các số ra khỏi queue theo thứ tự FIFO và thông báo số đó chẵn hay lẻ
import random 
class node : 
    def __init__(self,da_ta) :
        self.data =da_ta
        self.next=None 
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def EnQueue(self,x):
        x= node(x)
        if self.head is None : 
            self.head=x 
            self.last=x
        else :
            self.last.next= x 
            self.last=x 
    def DeQuece(self):
        if self.head is None: return None 
        else : 
            cur=self.head 
            next_cur =cur.next 
            if next_cur is None :
                self.head= None 
                self.last= None 
            else : 
                self.head=next_cur
                cur.next=None
            return cur.data 
    def Front(self):
        if self.head is not None:
            return self.head
        return None 
    def Empty(self):
        if self.head is None :return True 
        else : return False 

n=10 
ds=Queue()
for i in range (n):
    i=random.randint(1,100)
    ds.EnQueue(i)
while ds.Empty() is False:
    i=ds.DeQuece()
    if i%2==0:
        print(i,"chan")
    else:
        print(i,'le')
    
