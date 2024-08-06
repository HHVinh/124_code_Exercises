def tinhTong(*agrs):
    tong = 0
    for i in agrs:
        tong += i
    return tong
print('1+2+3 = {}'.format(tinhTong(1,2,3)))
