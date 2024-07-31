try:
    soThu1 ,phepTinh, soThu2 = input('Nhập số thứ 1, phép tính, số thứ 2 cách nhau bằng khoảng trắng: ').split()
    soThu1 = float(soThu1)
    soThu2 = float(soThu2)

    ketQua = None

    if phepTinh == '+':
        ketQua = soThu1 + soThu2
    elif phepTinh == '-':
        ketQua = soThu1 - soThu2
    elif phepTinh == '*':
        ketQua = soThu1 * soThu2
    elif phepTinh == ':' or phepTinh == '/':
        if soThu2 == 0:
            print('Số thứ 2 phải khác 0')
        else:
            ketQua = soThu1 / soThu2
    else:
        print('Phép tính chưa đúng')
    print(f'Kết quả của {soThu1} {phepTinh} {soThu2} là: ',ketQua)
except:
    print('Dữ liệu đầu vào không hợp lệ')