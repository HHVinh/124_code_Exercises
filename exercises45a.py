def tinh_Tong(a):
    if a == 0:
        return 0
    else:
        return a + tinh_Tong(a-1)
try:
    a = int(input('Nhập số tự nhiên bất kì: '))
    if a < 0:
        print('Nhập số tự nhiên từ 0 trở lên')
    elif a == 0:
        print(0)
    else:
        print(f'Tổng các số từ 1 đến {a} là: {tinh_Tong(a)}')
except:
    print('Dữ liệu nhập vào chưa phù hợp')