def dan_Xen_Chuoi(s1,s2):
    daoNguocChuoiS2 = s2[::-1]
    maXDoDaiChuoi = max(len(s1),len(s2))
    chuoiDanXen = ''

    for i in range(maXDoDaiChuoi):
        if (i < len(s1)):
            chuoiDanXen += s1[i]
        if (i < len(s2)):
            chuoiDanXen += daoNguocChuoiS2[i]
    return chuoiDanXen

s1 = input('Nhập chuỗi thứ nhất: ')
s2 = input('Nhập chuỗi thứ hai: ')

print(dan_Xen_Chuoi(s1,s2))