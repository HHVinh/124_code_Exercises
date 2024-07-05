# Import thư viện math
import math

print('Nhập 3 số từ bàn phím:')
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
        if delta > 0