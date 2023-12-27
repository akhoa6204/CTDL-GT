class node : 
    def __init__(self,da_ta):
        self.data = da_ta
        self.next = None 
        self.prev = None
class Box: 
    def __init__(self): 
        self.head = None
        self.last = None
    def add(self, x): 
        x=node(x)
        if self.head is not None: 
            self.last.next = x 
            self.last = x
        else : 
            self.head = x
            self.last = x
    def remove(self):
        cur = self.head
        pre = None 
        while cur != self.last and self.head is not None:
            pre = cur 
            cur = cur.next 
        if cur == self.head: 
            self.head = None 
            self.last = None
        else :
            self.last = pre 
            pre.next = None 
class Text:
    def __init__(self):
        self.head = None
        self.last = None
        self.box = Box()
    def type ( self,x):
        x = node (x)
        if self.head is not None:
            self.last.next = x 
            x.prev = self.last
            self.last = x
        else : 
            self.head = x 
            self.last = x
    def undo(self):
        if self.last is None : 
            return None 
        cur = self.last 
        if cur == self.head :
            self.head = None 
            self.last = None
            self.box.add(cur) 
        else :
            pre = cur.prev 
            pre.next = None 
            self.last = pre 
            self.box.add(cur) 
        x=self.head
        while x is not None: 
            print(x.data,end=' ')
            x=x.next
        print()
        
    def redo(self):
        if self.box.last is not None:
            self.type(self.box.last.data.data)
        x=self.head
        while x is not None: 
            print(x.data,end=' ')
            x=x.next
        print()
        self.box.remove()
text=Text()
text.type('khoa') 
text.type('anh')
text.type('khoa') 
text.type('anh')
text.type('khoa') 
text.type('anh')
text.undo()
text.undo()
text.undo()
text.undo()
text.undo()
text.undo()
text.undo()
text.undo()
text.redo()
text.redo()
text.redo()
text.redo()
text.redo()
text.redo()





            