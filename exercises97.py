def tuple_New(n):
    tupleCon = tuple(range(n))
    tupleKetQua = (n, tupleCon)
    print(tupleKetQua)
try:
    n = int(input('Nhập só tự nhiên bất kì: '))
    if n <0:
        print('Hãy nhập một số nguyên dương')
    else:
        tuple_New(n)
except:
    print('Dữ liệu đầu vào sai định dạng')