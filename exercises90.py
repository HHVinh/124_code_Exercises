def phan_Tu_Rieng(s):
    phanTuRieng = [i for i in s if s.count(i)==1]
    return phanTuRieng

dS1 = input('Hãy nhập dữ liệu chuỗi 1 bất kì: ').split()
dS2 = input('Hãy nhập dữ liệu chuỗi 2 bất kì: ').split()

if len(dS1) == 0 and len(dS2) == 0:
    print('Cả hai dữ liệu đều rỗng')
else:
    s = dS1 + dS2
    ketQua = phan_Tu_Rieng(s)
    if ketQua == []:
        print('Hai chuỗi trùng nhau, không có phần tử riêng')
    else:
        print(*ketQua)
