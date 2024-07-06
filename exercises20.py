# Import thư viện math
import math

print('Nhập 3 số từ bàn phím và cách nhau bởi khoảng trắng:')
try:
    a,b,c = map(float, input().split())

# Kiểm tra các trường hợp của bài toán
    if a == 0:
        if b == 0:
            if c == 0:
                print('Phương trình có vô số nghiệm')
            else:
                print('Phương trình vô nghiệm')
        else:
            print('Phương trình có 1 nghiệm duy nhất: \n x = {}'.format(-c/b))
    else:
        # Tính Delta
        delta = a*a - 4*a*c
        # Kiểm tra các trường hợp của delta
        if delta > 0:
            x1 = float((-b + math.sqrt(delta))/(2*a))
            x2 = float((-b - math.sqrt(delta))/(2*a))
            print('Phương trình có 2 nghiệm phân biệt là: \nx1 = {} \nx2 ={}'.format(x1,x2))
        elif delta == 0:
            x = -b/(2*a)
            print('Phương trình có nghiệm kép: \n x1 = x2 = {}'.format(x))
        else:
            print('Phương trình vô nghiệm')
except:
    print('Dữ liệu nhập vào chưa chính xác')


