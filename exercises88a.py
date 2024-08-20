def hoan_Doi_Chuoi(chuoi1,chuoi2):
    nuaDoDaiC1 = len(chuoi1)//2
    nuaDoDaiC2 = len(chuoi2)//2
    
    nuaSauChuoi1 = chuoi1[nuaDoDaiC1:]
    nuaSauChuoi2 = chuoi2[nuaDoDaiC2:]

    chuoi1 = chuoi1[:nuaDoDaiC1] + nuaSauChuoi2
    chuoi2 = chuoi2[:nuaDoDaiC2] + nuaSauChuoi1

    return chuoi1, chuoi2

chuoi1 = input('Nhập chuỗi thứ nhất bất kì: ').split()
chuoi2 = input('Nhập chuỗi thứ hai bất kì: ').split()

if not chuoi1 and not chuoi2:
    print('Cả hai chuỗi đều rỗng')

ketQua1, ketQua2 = hoan_Doi_Chuoi(chuoi1,chuoi2)
print(*ketQua1)
print(*ketQua2)