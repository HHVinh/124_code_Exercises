import math
try:
    a = int(input('Nhập số cần kiểm tra: '))
    if a < 2:
        print('Nhập một số nguyên lớn hơn 1')
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if a % i == 0:
                print(f'{a} không là số nguyên tố')
                break
        else:
                print(f'{a} là số nguyên tố')
except:
    print('Dữ liệu đầu vào không hợp lệ')