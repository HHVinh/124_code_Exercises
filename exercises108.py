def xoa_Ptu(setA):
    setB = setA.copy()
    for i in setB:
        if i.isdigit():
            setA.remove(i)
    return setA

setA = set(input('Nhập dữ liệu bất kì: ').split())
ketQua = xoa_Ptu(setA)

print('Dữ liệu còn lại sau khi xóa các số là: ', ketQua)