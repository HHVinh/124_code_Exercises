def sap_Xep_So(s):
    dsSO = []
    while s:
        giaTriNhoNhat = min(s)
        dsSO.append(giaTriNhoNhat)
        s = [x for x in s if x != giaTriNhoNhat]
    return dsSO
s = input('Nhập dãy số bất kì: ').split()
if len(s) == 0:
    print('Hãy nhập dữ liệu số bất kì')
else:
    try:
        dsSo = list(map(float,s))
        ketQua = sap_Xep_So(dsSo)
        print(*ketQua)
    except:
        print('Dữ liệu đầu vào chưa hợp lệ')