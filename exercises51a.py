import math
def kiem_Tra_So(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def so_Nguyen_To(a,b):
    for i in range(a, b+1):
        if kiem_Tra_So(i):
            print(i, end=' ')

try:
    a,b = map(int,input('Nhập số thứ nhất và số thứ hai: ').split())
    if a < 2 and a > b:
        print('Hãy nhập số thứ nhất lớn 1 và nhỏ hơn số thứ 2')
    else:
        so_Nguyen_To(a,b)
except:
    print('Dữ liệu nhập vào không hợp lệ')