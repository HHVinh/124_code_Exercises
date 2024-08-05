try:
    a = int(input('Nhập số tự nhiên muốn tính: '))
    if a < 0:
        ketQua = 'Nhập số nguyên dương'
    elif a == 0:
        ketQua = 0
    elif a == 1:
        ketQua = 1
    else:
        soThu1, soThu2 = 0 , 1
        for i in range(2,a+1):
            soThu1, soThu2 = soThu2, soThu1 + soThu2
            ketQua = soThu2
    print(f'Số Fibonacci của {a} = {ketQua}')
except:
    print('Dữ liệu nhập vào không hợp lệ')

