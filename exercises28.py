print('Nhập số tự nhiên từ 1 đến 9:')
a = int(input())
try:
    for i in range(1,10):
        print('{} x {} = {}'.format(a,i, a*i))
except:
    print('Hãy nhập số nguyên từ 1 đến 9')