try:
    a = int(input('Nhập số tự nhiên cần tính giai thừa: '))
    if a < 1:
        print('Nhập các số nguyên lớn hơn 0!')
    else:
        ketQua = 1
        for i in range(1, a+1):
            ketQua *= i
        print(f'{a} giai thừa có kết quả là:',ketQua)
except:
    print('Dữ liệu nhập vào không hợp lệ')