class Sinhvien:
    def __init__(self, ma, hoten, d1, d2):
        self.MaSV = ma
        self.HoTen = hoten
        self.Diem1 = d1
        self.Diem2 = d2
        self.DiemTB = None
        self.HL = None
        self.tiep=None

    def printSinhVien(self):
        print('[', self.MaSV, ']', '[', self.HoTen, ']', '[', self.Diem1, ']', '[', self.Diem2, ']', '[', self.DiemTB, ']', '[', self.HL, ']')

    def TinhTBSinhVien(self):
        if self.Diem1 is not None and self.Diem2 is not None:
            self.DiemTB = (self.Diem1 + self.Diem2) / 2

class DSSinhVien:
    def __init__(self):
        self.head=None
        self.last=None

    def ThemSinhVien(self, ma, ten, d1, d2):
        newStudent = Sinhvien(ma, ten, d1, d2)
        # thay self.DSSV.append(newStudent)
        if self.head==None: #DS rỗng
          self.head= newStudent
          self.last=newStudent
        else:  # không rỗng
          self.last.tiep=newStudent
          self.last=newStudent

    def inDSSinhVien(self):
        p=self.head
        while p is not None:
          p.printSinhVien()
          p=p.tiep

    def tinhTBSV(self):
        p=self.head
        while p is not None:
          p.TinhTBSinhVien()
          p=p.tiep

    def TBDiem1(self):
        Tongmon1 = 0
        for sv in self.DSSV:
            if sv.Diem1 is not None:
                Tongmon1 += sv.Diem1

        return Tongmon1 / len(self.DSSV)

    def xepHocLuc(self):
        for sv in self.DSSV:
            if sv.DiemTB is not None:
                if sv.DiemTB >= 9:
                    sv.HL = "Xuất sắc"
                elif sv.DiemTB >= 8:
                    sv.HL = "Giỏi"
                elif sv.DiemTB >= 6.5:
                    sv.HL = "Khá"
                elif sv.DiemTB >= 5.0:
                    sv.HL = "Trung Bình"
                else:
                    sv.HL = "Yếu"

    def XoaSinhVien(self, maSV):
        for sv in self.DSSV:
            if sv.MaSV == maSV:
                self.DSSV.remove(sv)
    def SXtheoTB(self):
      print("---Danh sach trước khi sx theo điểm TB---")
      self.inDSSinhVien()
      n=len(self.DSSV)
      for i in range(0,n-1):
        for j in range (i+1,n):
            if DSSV[i].DiemTB> DSSV[j].DiemTB:
                ss= DSSV[i]
                DSSV[i]=DSSV[j]
                DSSV[j]=ss
      print("Danh sach sau khi sx theo điểm TB")
      self.inDSSinhVien()

    def CapnhatSinhVien(self, maSV):
        for sv in self.DSSV:
            if sv.MaSV == maSV:
                print("Nhập thông tin mới cho sinh viên có mã", maSV)
                ten = input("Họ và tên: ")
                d1 = float(input("Điểm môn 1: "))
                d2 = float(input("Điểm môn 2: "))
                sv.HoTen = ten
                sv.Diem1 = d1
                sv.Diem2 = d2

# Example usage:
QLSV = DSSinhVien()
ToDo = 1
print('\n   *********************************************************')
print('   *                            * M E N U *                            *')
print('   *   1. Them sinh vien                         *')
print('   *   2. Xoa sinh vien                           *')
print('   *   3. Sua sinh vien                           *')
print('   *   4. Xem danh sach sinh vien                 *')
print('   *   5. Tinh diem trung binh cho tung sinh vien  *')
print('   *   6. Tinh diem trung binh mon1, mon2 cua toan bo sinh vien *')
print('   *   11. Xep loai hoc luc cho tung sinh vien *')
print('   *   0. Thoat khoi chuong trinh  *')
print('>>>', end=' ')
while ToDo != 0:
    ToDo = int(input("xin mời chọn chức năng: "))
    if ToDo == 0:
        break
    elif ToDo == 1:
        ma = input("Nhập mã sinh viên: ")
        ten = input("Họ và Tên : ")
        d1 = int(input("Điểm môn 1: "))
        d2 = int(input("Điểm môn 2: "))
        QLSV.ThemSinhVien(ma,ten,d1,d2)
        print("Da them 1 sinh vien.")
    elif ToDo == 2:
        maSV = input("Nhap ma sinh vien cua SV muon xoa: ")
        QLSV.XoaSinhVien(maSV)
    elif ToDo == 3:
        maSV = input("Nhap ma sinh vien cua SV muon sua thong tin: ")
        QLSV.CapnhatSinhVien(maSV)
    elif ToDo == 4:
        print("Danh sach sinh vien:\n")
        print('[ MaSV ]','[ Họ và Tên ]','[ Điểm 1 ]', '[ Điểm 2 ]', '[ Điểm TB ]', '[ Học Lực]')
        QLSV.inDSSinhVien()
    elif ToDo == 5:
        QLSV.tinhTBSV()
        print("Diem trung binh cua toan bo sinh vien da duoc tinh.")
    elif ToDo == 6:
        QLSV.TBDiem1_2()
        print("Diem trung binh mon1, mon2 cua toan bo sinh vien:", QLSV.TBDiem1_2())
    elif ToDo == 11:
        QLSV.xepHocLuc()
        print("Toan bo sinh vien da duoc xep hoc luc.")
    