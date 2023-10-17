class node: 
    def __init__(self,da_ta):
        self.data=da_ta
        self.next=None 
class Book: 
    def __init__(self,Title,Author,ISBN):
        self.title=Title
        self.author=Author
        self.isbn=ISBN
class Main : 
    def __init__(self):
        self.head=None 
        self.last=None 
    def Add(self,title,author,isbn): 
        newbook=Book(title,author,isbn)
        book=node(newbook)
        if self.head is None : 
            self.head=book 
            self.last=book
        else: 
            self.last.next  = book
            self.last=book 
    def Print(self):
        cur = self.head
        while cur is not  None :
            print(cur.data.title,cur.data.author,cur.data.isbn,end=' ')
            if cur != self.last :
                print('|',end=' ')
            cur = cur.next
        print()
    def Remove(self,name):
        cur=self.head
        pre = None 
        while cur.data.title != name and self.head!= None : 
            pre =cur 
            cur = cur.next 
        if cur == self.head : 
            self.head=cur.next
            cur.next=None 
        elif cur== self.last : 
            self.last= pre 
            pre.next= None 
        else: 
            pre.next=cur.next 
            cur.next = None 
        del cur 
    def Find(self,name):
        cur=self.head
        i=1
        while cur.data.title != name and self.head!= None : 
            cur =cur.next
            i+=1 
        print('Số thứ tự:',i)

main=Main()
main.Add(input('Title: '),input('Author: '),int(input('ISBN: ')))
main.Add(input('Title: '),input('Author: '),int(input('ISBN: ')))
main.Add(input('Title: '),input('Author: '),int(input('ISBN: ')))
main.Print()
main.Remove(input('Title cần xóa: '))
main.Print()
main.Find(input('Title cần tìm: '))

                    