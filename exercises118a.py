def xoa_Ptu_Trung(l1,l2):
    list1 = []
    list2 = []
    for ptu in l2:
        if ptu not in list2:
            list2.append(ptu)
            viTri = l2.index(ptu)
            list1.append(l1[viTri])
    dictKetQua = dict(zip(list1,list2))
    return dictKetQua

l1 = input('Hãy nhập các giá trị key cho dict: ').split()
l2 = input('Hãy nhập các giá trị value cho dict: ').split()

if len(l1) != len(l2):
    print('Hãy nhập số lượng key và value bằng nhau')
else:
    dictKetQua = xoa_Ptu_Trung(l1,l2)
    print(dictKetQua)