def kiem_Tra_So(n):
    ketQua = 0
    for i in range(1,n//2 + 1):
        if n % i ==0:
            ketQua += i
    if n == ketQua:
        return True
    return False

def so_Hoan_Thien(n):
    for i in range(1,n):
        if kiem_Tra_So(i):
            print(i, end=' ')
        
try:
    n = int(input('Nhập số tự nhiên bất kì: '))
    if n < 0:
        print('Nhập số tự nhiên lớn hơn không')
    else:
        so_Hoan_Thien(n)
except:
    print('Dữ liệu đầu vào không hợp lệ')

