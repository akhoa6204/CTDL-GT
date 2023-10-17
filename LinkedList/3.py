class node: 
    def __init__(self,da_ta):
        self.data=da_ta
        self.next=None 
class Book: 
    def __init__(self,Title,Author,ISBN):
        self.title=Title
        self.author=Author
        self.isbn=ISBN
class Main: 
    def __init__(self):
        self.head=None
        self.last=None
    def Print(self): 
        cur=self.head
        while cur != None  : 
            print(cur.data.title,cur.data.author,cur.data.isbn,end=' ')
            if cur != self.last:
                print('|',end=' ')
            cur=cur.next
        print()
    def Add(self,name): 
        name=node(name)
        if self.head is not None: 
            self.last.next=name 
            self.last=name 
        else : 
            self.head=name
            self.last=name
    def Remove(self,name):
        cur=self.head
        pre =None 
        while cur.data !=name and self.head is not None: 
            pre=cur 
            cur=cur.next 
        if cur== self.head: 
            self.head=cur.next 
            cur.next=None 
        elif cur== self.last: 
            self.last= pre
            pre.next=None 
        else: 
            pre.next= cur.next
            cur.next= None 
        del cur
    def Find(self,name):
        i=0
        cur=self.head
        while cur.data !=name and self.head is not None: 
            cur=cur.next
            i+=1
        print('Số thứ tự',i)
book1=Book('toan','khoa','123')  
book2=Book('hoa','ngoc','456')
book3=Book('ly','bo','789')
main=Main()
main.Add(book1)
main.Add(book2)
main.Add(book3)
main.Print()
main.Remove(book1)
main.Print()
main.Find(book3)

  
                    