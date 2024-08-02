try:
    a = int(input('Nhập số nguyên từ 1 đến 9: '))
    if a <1 or a >9:
        print('Dữ liệu nhập vào phải là số nguyên từ 1 đến 9!')
    else:
        for i in range(1,10):
            print(f'{a} * {i} = ',a*i)
except:
    print('Nhập số nguyên')