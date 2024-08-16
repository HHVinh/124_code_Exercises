def dao_Nguoc_Ki_Tu(s):
    kiTu = list(s)
    daoNguocKiTu = kiTu[::-1]
    return daoNguocKiTu

s = input('Nhập dữ liệu bất kì: ')
ketQua = dao_Nguoc_Ki_Tu(s)

print(*ketQua)
