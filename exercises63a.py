def thay_Nguyen_Am(s):
    nguyenAm = "oaeuiOAEUI"
    tongNguyenAm = 0
    for i in nguyenAm:
        tongNguyenAm += s.count(i)
        s = s.replace(i,'$')
    return tongNguyenAm, s

s = input('Nhập chuỗi kí tự bất kì: ')
tongNguyenAm, ketQua = thay_Nguyen_Am(s)

print(tongNguyenAm)
print(ketQua)
