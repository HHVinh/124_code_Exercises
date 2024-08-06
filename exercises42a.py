def tenTuoi(a,b):
    print(f'Xin chào, tôi tên là {a} và tôi {b} tuổi')

try:
    a = input('Hãy nhập tên của bạn: ')
    b = int(input('Hãy nhập tuổi của bạn: '))
    if b <1:
        print('Hãy nhập tuổi lớn hơn 0')
    else:
        tenTuoi(a,b)
except:
    print('Dữ liệu đầu vào không hợp lệ')