def tao_Dict():
    l1 = input('Nhập dữ liệu cho các key: ').split()
    try:
        l2 = list(map(int,input('Nhập dữ liệu cho các value: ').split()))
    except:
        print('Các value phải là số nguyên')
        return None
    
    if len(l1) == len(l2):
        dictKetQua = dict(zip(l1,l2))
    else:
        print('Số lượng của key và value phải giống nhau')
        return None
    return dictKetQua

def xep_Value(dictA):
    listItem = dictA.items()
    listItemSorted = sorted(listItem, key=lambda item: item[1])
    dictKetQua = dict(listItemSorted)
    return dictKetQua

dictA = tao_Dict()
dictB = xep_Value(dictA)

print(dictA)
print(dictB)
