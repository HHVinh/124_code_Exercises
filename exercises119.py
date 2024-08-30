def nhap_Dict(l1,l2):
    dictKetQua = dict(zip(l1,l2))
    return dictKetQua

l1 = input('Hãy nhập các giá trị key của dict: ').split()
try:
    l2 = list(map(int,input('Hãy nhập các giá trị value cho dict: ').split()))
    if len(l1) != len(l2):
        print('Hãy nhập số lượng của key và value bằng nhau')
    else:    
        chuoiKey = '-'.join(l1)
        dictKetQua = nhap_Dict(l1, l2)
        tongGtri = sum(l2)
        print('Dict kết quả là: ',dictKetQua)
        print('Chuỗi các key là: ',chuoiKey)
        print('Tổng các value là: ',tongGtri)
except:
    print('Hãy nhập các giá trị value là số nguyên')


