import math

def bac_1(a,b):
    if a == 0:
        if b == 0:
            return 'Phương trình vô số nghiệm'
        else:
            return 'Phương trình vô nghiệm'
    else:
        return -b/a
    
def bac_2(a,b,c):
    if a == 0:
        return bac_1(b,c)
    delTa = b*b - 4*a*c
    if delTa == 0:
        x = -b/(2*a)
        return f'Phương trình có nghiệm kép x1 = x2 = {x}'
    elif delTa < 0:
        return 'Phương trình vô nghiệm'
    else:
        x1 = (-b + math.sqrt(delTa))/(2*a)
        x2 = (-b - math.sqrt(delTa))/(2*a)
        return f'Phương trình có 2 nghiệm phân biệt là:\nx1 = {x1}\nx2 = {x2}'
        
try:
    n = int(input('Nhập số 1 hoặc 2: '))
    if n == 1 or n ==2:
        if n == 1:
            a,b = map(float,input('Nhập hệ số a và b: ').split())
            print(f'Phương trình {a}x + {b} = 0 có kết quả là:\n{bac_1(a,b)}')
        elif n == 2:
            a,b,c = map(float,input('Nhập hệ số a, b và c: ').split())
            print(f'Phương trình {a}x^2 + {b}x + {c} = 0 có kết quả là:\n{bac_2(a,b,c)}')
    else:        
        print('Nhập số 1 hoặc 2')
except:
    print('Dữ liệu đầu vào không hợp lệ')

