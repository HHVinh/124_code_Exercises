while True:
    try:
        ten1 = input('Nhập tên bạn 1: ')
        chieuCao1 = int(input('Nhập chiều cao bạn 1 (cm): '))
        ten2 = input('Nhập tên bạn 1: ')
        chieuCao2 = int(input('Nhập chiều cao bạn 2 (cm): '))
        break
    except:
        print('Dữ liệu đầu vào không hợp lệ')
if chieuCao1 > chieuCao2:
    print(f'Bạn {ten1} cao hơn bạn {ten2}')
elif chieuCao1 < chieuCao2:
    print(f'Bạn {ten2} cao hơn bạn {ten1}')
else:
    print('Hai bạn cao bằng nhau')
