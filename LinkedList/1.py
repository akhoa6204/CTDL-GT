import random 
class node : 
    def __init__(self,da_ta):
        self.data=da_ta
        self.next=None 
class Playlist:
    def __init__(self):
        self.head=None      
        self.last=None
    def Print(self):
        cur=self.head
        kq=''
        while cur != None: 
            kq+=str(cur.data)
            if cur !=self.last:
                kq+=' -> '
            cur=cur.next
        print (kq)     
    def Add(self,name):
        name=node(name)
        if self.head is None:
            self.head=name
            self.last=name
        else : 
            self.last.next=name
            self.last=name        
    def Remove(self,name):
        cur =self.head 
        pre = None 
        while cur is not None and cur.data != name:
            pre =cur 
            cur=cur.next 
        if cur is not None: #tìm thấy
            if cur== self.head and cur == self.last :#xóa phần tử duy nhất
                self.head=None 
                self.last =None 
            elif cur == self.head :
                self.head=cur.next
                cur.next=None
            elif cur == self.last :
                self.last=pre 
                pre.next=None
            else : # xóa ở giữa 
                pre.next = cur.next 
                cur.next= None 
        del cur
    def RemoveAll (self):
        cur=self.head 
        while cur !=None : 
            tam=cur 
            cur=cur.next 
            del tam
        self.head=None
        self.last=None
    def Shuffle(self):
        count=0 
        cur=self.head 
        while cur!=None: 
            count+=1
            cur=cur.next
        L=[None]*count
        cur=self.head 
        i=0
        while cur!=None: 
           L[i]=cur 
           cur=cur.next
           i+=1
        for i in range(count - 1, 0, -1): #giải thuật Fisher-Yates
            j = random.randint(0, i)
            L[i], L[j] = L[j], L[i] 
            # Thuật toán Fisher-Yates hoạt động như sau:
            # Bắt đầu từ phần tử cuối cùng của mảng (hoặc danh sách).
            # Chọn một phần tử ngẫu nhiên từ phần tử hiện tại đến phần tử đầu tiên của mảng.
            # Hoán đổi phần tử được chọn với phần tử cuối cùng của mảng (hoặc danh sách).
            # Giảm kích thước của mảng đi một đơn vị, giảm loại trừ phần tử cuối cùng, vì nó đã được "xác định" và không thể thay đổi vị trí nữa.
            # Lặp lại quy trình với các phần tử còn lại cho đến khi chỉ còn một phần tử.
        self.RemoveAll()
        for i in range(len(L)): 
            self.Add(L[i].data)  
    def Next(self,now):
        i=0 
        cur =self.head 
        pre=None
        while i<now and self.head != None :    
                i+=1 
                pre=cur 
                cur=cur.next 
        if cur != self.last :
            return cur.data 
        return pre.data  
    def Pre(self,now):
        i=0 
        cur =self.head 
        pre=None    
        while i<now and self.head != None:
            i+=1 
            pre = cur 
            cur=cur.next 
        if cur != self.head : 
            return pre.data
        return cur.data 
music=Playlist()
music.Add(1)
music.Add(2)
music.Add(3)
music.Add(4)
print(music.Next(3))
print(music.Pre(0))
music.Shuffle()
music.Print()                 