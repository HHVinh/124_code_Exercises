# Nhập biểu thức từ bàn phím
print('Nhập số thứ nhất, phép tính, số thứ 2:')
try:
    soThu1, phepTinh, soThu2 = input().split()

    # Ép kiểu dữ liệu
    soThu1 = float(soThu1)
    soThu2 = float(soThu2)

    # Tạo biến lưu kết quả
    ketQua = None

    # Dùng câu lệnh rẽ nhánh để phân loại phép tính:
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
        print('Biểu thức không hợp lệ')

    # In kết quả ra màn hình
    if ketQua != None:
        print('{} {} {} = {}'.format(soThu1,phepTinh,soThu2,ketQua))
except:
    print('Biểu thức chưa đúng định dạng')
