import math
try:
    a , b = map(int,input('Nhập 2 số cách nhau bởi khoảng trắng: ').split())
    if a <2 or b <2:
        print('Hãy nhập hai số lớn hơn 1')
    elif a>b:
        print('Hãy nhập số thứ hai lớn hơn số thứ nhất')
    else:
        for i in range(a,b+1):
            for j in range(2,int(math.sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                print(i, end=' ')
except:
    print('Dữ liệu nhập vào không hợp lệ')