def list_To_Dict(list1, list2):
    dictKetQua  = dict(zip(list1,list2))
    return dictKetQua

list1 = list(input('Nhập dữ liệu bất kì cho list1: ').split())
list2 = list(input('Nhập dữ liệu bất kì cho lis1t2 ').split())

if len(list1) == len(list2):
    dictKetQua = list_To_Dict(list1, list2)
    print(dictKetQua)
    for key, value in dictKetQua.items():
        print(f'{key}: {value}')
else:
    print('Cả 2 list phải có cùng số lượng giá trị')