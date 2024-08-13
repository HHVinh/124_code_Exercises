def xoa_Trung_Lap(s):
    ketQua = ''
    for i in s:
        if i not in ketQua:
            ketQua += i
    return ketQua

s = input('Nhập dữ liệu bất kì: ')
print(xoa_Trung_Lap(s))