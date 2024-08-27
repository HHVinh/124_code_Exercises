def kiem_Tra_Set(setA):
    if len(setA) % 2 == 0:
        setA.clear()
    return setA

setA = set(input('Nhập dữ liệu bất kì: ').split())
setA = kiem_Tra_Set(setA)
print(setA)