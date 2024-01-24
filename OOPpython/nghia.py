class sinhvien: 
    def __init__(self, id, name, tp1, tp2):
        self.id = id 
        self.name = name 
        self.Class = id[7:9] + "." + id[10]
        self.tp1 = tp1
        self.tp2 = tp2 
        self.dtb = None
        self.grade = None
    
    def Print(self):    
        print(f"[ {self.id} ] [ {self.name} ] [ {self.Class} ] [ {self.tp1} ] [ {self.tp2} ]", end= " ")
        if self.dtb is not None: 
            print(f"[ {self.dtb} ]",end = " ")
            if self.grade is not None: 
                print(f"[ {self.grade} ]")
            else: print()
        else: print()


class dssv:
    def __init__(self): 
        self.ds = [] 
    
    def them(self, sv): 
        self.ds.append(sv)

    def xoa(self, id) :
        for sv in self.ds: 
            if sv.id == id:
                self.ds.remove(sv)
                print("Đã xóa sinh viên")
                break
        else: print("Không tồn tại sinh viên trong danh sách")
    def Print_ds(self):
        print("<<<-----Danh sách sinh viên-----")
        for sv in self.ds: 
            sv.Print()
        print("----------------------------->>>")
    def sua(self, id):
        for sv in self.ds:
            if sv.id == id:
                print("Thuộc tính cần sửa")
                print("1: id")
                print("2: name")
                print("3: class")
                print("4: tp1")
                print("5: tp2")
                print("0: thoát")
                while True:
                    n = int(input())
                    if n == 0:
                        break
                    elif n == 1: 
                        print("id: ",end = "")
                        sv.id = int(input())
                        break
                    elif n == 2:
                        print("name: ",end = "")
                        sv.name = input()
                        break
                    elif n == 3:
                        print("class: ",end = "")
                        sv.Class = input()
                        break
                    elif n == 4:
                        print("tp1: ",end = "")
                        sv.tp1 = float(input())
                        break
                    elif n == 5:
                        print("tp2: ",end = "")
                        sv.tp2 = float(input())
                        break
    def dtbAll(self): 
        for sv in self.ds:
            sv.dtb = (sv.tp1 + sv.tp2) / 2
        print("Đã tính điểm trung bình toàn bộ sinh viên")
    def dtbtpAll(self):
        tong = 0
        for sv in self.ds:
            tong += sv.tp1 
        print(f"Điểm tb tp1 của toàn bộ sinh viên: {tong/len(self.ds)}")
        tong = 0 
        for sv in self.ds:
            tong += sv.tp2
        print(f"Điểm tb tp2 của toàn bộ sinh viên: {tong/len(self.ds)}")
    def min(self):
        min = self.ds[0].dtb
        for sv in self.ds:
            if sv.dtb < min :
                min = sv.dtb
        for sv in self.ds:
            if sv.dtb == min: 
                sv.Print()
    def max(self):
        max = self.ds[0].dtb
        for sv in self.ds:
            if sv.dtb > max:
                max = sv.dtb
        for sv in self.ds:
            if sv.dtb == max: 
                sv.Print()
    def xeploai(self):
        for sv in self.ds:
            if sv.dtb >= 8.5:
                sv.grade = "Học lực giỏi"
            elif sv.dtb >= 7:
                sv.grade = "Học lực Khá"
            elif sv.dtb >= 5.5:
                sv.grade = "Học lực Trung bình"
            elif sv.dtb >= 4:
                sv.grade = "Học lực Yếu"
            else : 
                sv.grade = "Học lực Kém"
        print("Đã xếp loại học lực cho toàn bộ sinh viên")
    def sapxep(self): 
        lops = []
        for sv in self.ds: 
            if sv.Class not in lops: 
                lops.append(sv.Class)
        for lop in lops: 
            print(f"-----{lop}-----") 
            tunglop =[]
            for sv in self.ds: 
                if sv.Class == lop: 
                    tunglop.append(sv) 
            for i in range(len(tunglop) - 1):
                for j in range (i + 1, len(tunglop)):
                    if tunglop[i].dtb < tunglop[j].dtb:
                        tunglop[i], tunglop[j] = tunglop[j], tunglop[i]   
            for sv in tunglop:
                sv.Print()
DS = dssv()
print('<<<-------------------------------------------------------------------')
print('*                               * M E N U *                          *')
print('*   1. Them sinh vien                                                *')
print('*   2. Xoa sinh vien                                                 *')
print('*   3. Sua sinh vien                                                 *')
print('*   4. Xem danh sach sinh vien                                       *')
print('*   5. Tinh diem trung binh cho tung sinh vien                       *')
print('*   6. Tinh diem trung binh mon1, mon2 cua toan bo sinh vien         *')
print('*   7. Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất    *')
print('*   8. Tìm xem sinh viên nào có điểm trung bình học tập cao nhất     *')
print('*   9. Sắp xếp danh sách sinh viên theo lớp                          *')
print('*   10. Xep loai hoc luc cho tung sinh vien                          *')
print('*   0. Thoat khoi chuong trinh                                       *')
print('------------------------------------------------------------------->>>')
while True :
    n = int(input("Chọn phương thức: "))
    if n == 0: 
        print("Dừng chương trình")
        break 
    elif n == 1: 
        while True:
            id = input("id: ")
            if len(id) == 12 and id.isdigit(): 
                break
            else: 
                print("id phải là số và có độ dài là 12")
        name = input("name: ")
        while True: 
            tp1 = float(input("tp1: "))
            tp2 = float(input("tp2: "))
            if 0 <= tp1 <= 10 and 0 <= tp2 <= 10:
                break 
            else : print("Điểm từ 0 - 10")
        for sv in DS.ds: 
            if id == sv.id: 
                print("Đã tồn tại id trong dssv")
                break
        else:
            sv = sinhvien(id, name, tp1, tp2)
            DS.them(sv) 
    elif n == 2: 
        id = int(input("id cần xóa: "))
        DS.xoa(id)
    elif n == 3: 
        id = int(input("id sinh viên cần sửa: "))
        for sv in DS.ds: 
            if id == sv.id: 
                DS.sua(id)
                break
        else: print("Không tồn tại sinh viên trong danh sách")
    elif n == 4:
        DS.Print_ds()
    elif n == 5: 
        DS.dtbAll()
    elif n == 6:
        DS.dtbtpAll() 
    elif n== 7: 
        DS.dtbAll()
        DS.min()
    elif n == 8:
        DS.dtbAll()
        DS.max()    
    elif n== 9: 
        DS.dtbAll()
        DS.sapxep()
    elif n == 10:
        DS.dtbAll()
        DS.xeploai()   