def them_List(setA, listB):
    for ptu in listB:
        setA.add(ptu)
    return setA

setA = set(input('Nhập dữ liệu bất kì: ').split())
listB = list(input('Nhập dữ liệu bất kì: ').split())

ketQua = them_List(setA,listB)

print('Dữ liệu sau khi được nối là: ', ketQua)