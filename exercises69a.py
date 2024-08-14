def ki_Tu_Khong_Trung(s):
    kiTuKhongTrung = ''
    for i in s:
        if i not in kiTuKhongTrung:
            kiTuKhongTrung += i
    return kiTuKhongTrung

def so_Lan_Xuat_Hien(s):
    chuoiKiTu = ki_Tu_Khong_Trung(s)
    for i in chuoiKiTu:
        soLanXuatHien = s.count(i)
        print(f"'{i}':{soLanXuatHien};",end='')

s = input('Nhập chuỗi bất kì: ')
so_Lan_Xuat_Hien(s)