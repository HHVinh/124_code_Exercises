def tuple_So_Tu_Nhien(n):
    tupleSTN = tuple(i for i in range(n))
    print(tupleSTN)

try:
    n = int(input('Nhập một số tự nhiên bất kì: '))
    if n < 0:
        print('Vui lòng nhập số nguyên dương')
    else:
        tuple_So_Tu_Nhien(n)
except:
    print('Dữ liệu đầu vào không hợp lệ')