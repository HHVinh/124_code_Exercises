try:
    a = int(input('Nhập số tự nhiên bất kì: '))
    if a < 0:
        print('Nhập số lớn hơn 0')
    else:
        soChan = 0
        soLe = 0
        while a > 0:
            if a % 2 ==0:
                soChan += a % 10
            else:
                soLe += a % 10
            a = a//10
        print(f'Tổng các số chẵn = {soChan}\nTổng các số lẻ = {soLe}')
except:
    print('Dữ liệu nhập vào chưa chính xác')