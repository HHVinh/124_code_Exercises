def kiem_Tra_Set(setA,setB):
    ptuChung = setA & setB
    ptuRieng = setA ^ setB
    return ptuChung,ptuRieng

setA = set(input('Nhập dữ liệu bất kì cho set1: ').split())
setB = set(input('Nhập dữ liệu bất kì cho set2: ').split())

ptuChung, ptuRieng = kiem_Tra_Set(setA,setB)

print('Phần tử chung của 2 set là: ', ptuChung)
print('Phần tử riêng của 2 set là: ', ptuRieng)

