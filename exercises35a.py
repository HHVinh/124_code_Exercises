try:
    a = int(input('Nhập số cần đảo ngược: '))
    if a < 0:
        print('Nhập só tự nhiên lớn hơn 0')
    else:
        ketQua = 0
        while a > 0:
            soDu = a % 10
            ketQua = ketQua *10 + soDu
            a = a // 10
        print(f' Số đảo ngược là {ketQua}')
except:
    print('Dữ liệu nhập vào không phù hợp')