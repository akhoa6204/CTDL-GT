class node: 
    def __init__(self,da_ta):
        self.data = da_ta
        self.next=None 
class To_Do :
    def __init__(self): 
        self.head = None
        self.last = None
    def Print(self):
        cur=self.head
        while cur is not None: 
            print(cur.data,end=' ')
            if cur !=self.last:
                print('->',end=' ')
            cur=cur.next
        print()
    def Add(self,name):
        name=node(name)
        if self.head !=None : 
            self.last.next =name 
            self.last=name 
        else : 
            self.head =name 
            self.last =name
    def Remove(self,name):
        cur=self.head
        pre=None 
        while cur!=name and self.head != None : 
            pre=cur
            cur=cur.next 
        if cur== self.head : 
            self.head=cur.next 
            cur.next = None
        elif cur== self.last:
            self.last=pre 
            pre.next=None
        else: 
            pre.next=cur.next 
            cur.next=None 
        del cur 
    def Complete(self,name):
        cur = self.head
        while cur.data !=name and self.head != None : 
            cur=cur.next
        cur.data =str(cur.data)+"✅"
work=To_Do()
work.Add(1)
work.Add(2)
work.Add(3)
work.Add(4)
work.Add(5)
work.Print()
work.Complete(2)
work.Print()



    