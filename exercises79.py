def day_So_Giam(s):
    soDauTien = s[0]
    for i in s:
        if i > soDauTien:
            return False
        soDauTien = i
    return True

s = input('Nhập dãy số bất kì: ').split()
if len(s) == 0:
    print('Hãy nhập số bất kì: ')
else:
    try:
        dsSo = list(map(float,s))
        ketQua = day_So_Giam(dsSo)
        print(ketQua)
    except:
        print('Dữ liệu nhập vào chưa hợp lệ')