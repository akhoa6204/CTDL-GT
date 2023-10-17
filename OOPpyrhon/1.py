class sinhvien:
    def __init__(self,MASV,HOTEN,DIEM1,Diem2):# hàm khởi tạo 
        self.masv = MASV
        self.hoten = HOTEN
        self.diem1 = DIEM1
        self.diem2 = Diem2
        self.DTB=None
        self.next=None
        self.hl=None
    def TinhTBSinhVien(self):
        if self.diem1 is not None and self.diem2 is not None:
            self.DiemTB = (self.diem1 + self.diem2) / 2
    def printSinhVien(self):
        print('[', self.masv, ']', '[', self.hoten, ']', '[', self.diem1, ']', '[', self.diem2, ']', '[', self.DiemTB, ']', '[', self.hl ,']')

class danhsach: # phải tạo đối tuọng thuộc lớp sinhvien thì mới dùng được được các chức năng của class sinhvien trong class khác
    def __init__(self):
        self.head=None
        self.last=None
    def ADD(self):
        sinhvien.masv=input("nhập mã sinh viên: ")
        sinhvien.hoten=input("Nhập họ tên: ")
        sinhvien.diem1=float(input("Nhập điểm thành phần 1: "))
        sinhvien.diem2=float(input("Nhập điểm thành phần 2: "))
        sv=sinhvien(sinhvien.masv,sinhvien.hoten,sinhvien.diem1,sinhvien.diem2) # tạo đối tượng
        # danhsach.DSSV.append(sv)
        if self.head==None: #DS rỗng
          self.head= sv
          self.last=sv
        else:  # không rỗng
          self.last.tiep=sv
          self.last=sv

    def DTB(self):
        sv=self.head 
        while sv is not None :
            sv.TinhTBSinhVien()
            sv=sv.next
        print("Điểm trung bình của từng sinh viên đã được tính")
    def PRINT(self):
        sv=self.head
        while sv is not None:
            sv.printSinhVien()
            sv=sv.next
    def ARRANGEDTB(self):
        # danhsach.DSSV.sort(key=lambda sv: sv.DTB)
        # sắp xếp nhận đối tượng sv và lấy dtb trong đối tượng sv để sắp xếp
        dem=0
        A=[]
        for sv in danhsach.DSSV:
            if sv.masv[7:10] not in A: 
                A.append(sv.masv[7:10])
                dem+=1
        B=[[] for i in range (dem)]
        for i in range(dem):
            for sv in danhsach.DSSV:
                if sv.masv[7:10] in A[i]:
                    B[i].append(sv.DTB) 
        for i in range(dem):
            B[i].sort()
            print(A[i]+":")
            print(*B[i]) 
    def CALCULATED1(self):
        tong=0
        sv=self.head 
        while sv is not None:
            tong+=sv.diem1 #lỗi 
        print(tong/len(danhsach.DSSV))
    def CALCULATED2(self):
        tong=0
        for sv in danhsach.DSSV:
            tong+=sv.diem2
        print(tong/len(danhsach.DSSV))
    def DELETE(self,masv):
        for sv in danhsach.DSSV:
            if sv.masv==masv:
                danhsach.DSSV.remove(sv)
                print("Sinh viên đã được xóa!!!")
                break
        else: print("Không tìm thấy sinh viên có mã như bạn yêu cầu")
    def FIX(self,masv):
        for sv in danhsach.DSSV:
            if sv.masv==masv:
                print("0: Dừng thay đổi\n1: Thay đổi mã sinh viên\n2: Thay đổi tên sinh viên\n3: Thay đổi điểm tp1\n4: Thay đổi điểm tp2")
                while True:
                    n=int(input())
                    if n==0:break
                    elif n==1:
                        sv.masv=int(input("Mã sinh viên: "))
                    elif n==2:
                        sv.hoten=input("Họ tên sinh viên: ")
                    elif n==3:
                        sv.diem1=float(input("Điểm tp1: "))
                        sv.DTB=(sv.diem1+sv.diem2)/2
                    elif n==4:
                        sv.diem2=float(input("Điểm tp2: "))
                        sv.DTB=(sv.diem1+sv.diem2)/2
    def MAX(self):
        max=danhsach.DSSV[0].DTB
        for sv in danhsach.DSSV:
            if sv.DTB>max:
                max=sv.DTB
        for sv in danhsach.DSSV:
            if sv.DTB==max:
                print(sv.masv,sv.hoten,sv.diem1,sv.diem2,sv.DTB)
    def MIN(self):
        min=danhsach.DSSV[0].DTB
        for sv in danhsach.DSSV:
            if sv.DTB <min:
                min=sv.DTB
        for sv in danhsach.DSSV:
            if sv.DTB==min:
                print(sv.masv,sv.hoten,sv.diem1,sv.diem2,sv.DTB)
    def XEPLOAI(self):
        for sv in danhsach.DSSV:
            if sv.DTB is not None :
                if sv.DTB>=8.5:print(sv.masv,sv.hoten,"Học lực Giỏi")
                elif sv.DTB>=7:print(sv.masv,sv.hoten,"Học lực Khá")
                elif sv.DTB>=5.5:print(sv.masv,sv.hoten,"Học lực Trung bình")
                elif sv.DTB>=4:print(sv.masv,sv.hoten,"Học lực Yếu")
                else : print(sv.masv,sv.hoten,"Học lực Kém")
            else: "Không đủ điểm thành phần!!!"

ds=danhsach()
print('''----------------------------------MENU----------------------------------
0: Thoát chương trình
1: Thêm sinh viên
2: Xóa sinh viên
3: Sửa sinh viên
4: In danh sách sinh viên
5: Tính điểm trung bình của từng sinh viên
6: Tính điểm trung bình cộng điểm tp1 của toàn bộ sinh viên
7: Tính điểm trung bình cộng điểm tp2 của toàn bộ sinh viên
8: Sinh viên có điểm trung bình cao nhất
9: Sinh viên có điểm trung bình thấp nhất
10: Xếp học lực sinh viên
11: Sắp xếp danh sách sinh viên thoe lớp và điểm trung bình
--------------------------------------------------------------------->>>''')
while True: 
    print("Xin mời bạn chọn chức năng")
    n=int(input())
    if n==0:
        break 
    elif n==1:
        ds.ADD()
    elif n==2:
        sv=input("Mã sinh viên cần xóa: ")
        ds.DELETE(sv)
    elif n==3: 
        sv=input("Mã sinh viên cần sửa: ")
        ds.FIX(sv)
    elif n==4: 
        ds.PRINT()
        print()
    elif n==5: 
        ds.DTB()
    elif n==6:
        ds.CALCULATED1()
    elif n==7:
        ds.CALCULATED2()
    elif n==8:
        ds.MAX()
    elif n==9:
        ds.MIN()
    elif n==10:
        ds.XEPLOAI()
    elif n==11:
        ds.ARRANGEDTB()


            
            
        