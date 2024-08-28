def ktra_Set(setA,setB):
    ptuRieng = setA ^ setB
    ptRiengA = setA & ptuRieng
    ptRiengB = setB & ptuRieng
    return ptRiengA, ptRiengB

setA = set(input('Nhập dữ liệu bất kì cho set1: ').split())
setB = set(input('Nhập dữ liệu bất kì cho set2: ').split())

ptRiengA, ptRiengB = ktra_Set(setA,setB)

print('Phần tử riêng của set1 là: ',ptRiengA)
print('Phần tử riêng của set2 là: ',ptRiengB)

