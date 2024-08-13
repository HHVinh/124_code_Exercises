def noi_Chuoi(s):
    tachChuoi = s.split()
    noiChuoi = '-'.join(tachChuoi)
    return noiChuoi

s = input('Nhập chuỗi dữ liệu bất kì: ')
print(noi_Chuoi(s))