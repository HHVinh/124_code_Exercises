def nhap_Dict(l1,l2):
    dictKetQua = dict(zip(l1,l2))
    return dictKetQua

def cap_Nhat_Dict(d1,d2):
    if len(d1) < len(d2):
        d2.update(d1)
        return d2
    d1.update(d2)
    return d1

l1 = list(input('Nhập các giá trị key cho dict1: ').split())
l2 = list(input('Nhập các giá trị value cho dict1: ').split())
l3 = list(input('Nhập các giá trị key cho dict2: ').split())
l4 = list(input('Nhập các giá trị value cho dict2: ').split())

if len(l1) != len(l2) or len(l3) != len(l4):
    print('Hãy nhập số lượng key và value của mỗi dict bằng nhau')
    
else:
    d1 = nhap_Dict(l1,l2)
    d2 = nhap_Dict(l3,l4)
    dictKetQua = cap_Nhat_Dict(d1,d2)
    print(dictKetQua)