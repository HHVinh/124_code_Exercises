def nhap_Dict():
    l1 = input('Nhập các giá trị key cho dict: ').split()
    l2 = input('Nhập các giá trị value cho dict: ').split()
    if len(l1) != len(l2):
        print('Hãy nhập số lượng key và value bằng nhau')
        return None
    dictKetQua = dict(zip(l1,l2))
    return dictKetQua

def xoa_Ptu_Trung(dictA):
    listValue = list()
    dictKetQua = dictA.copy()
    for key, value in dictA.items():
        if value in listValue:
            dictKetQua.pop(key)
        else:
            listValue.append(value)
    return dictKetQua

dictA = nhap_Dict()
if dictA is not None:
    dictKetQua = xoa_Ptu_Trung(dictA)
    print(dictKetQua)
else:
    print('Dữ liệu không hợp lệ')