def chen_Tu(danhSach, n):
    ketQua = []  # Danh sách rỗng
    for i in range(len(danhSach)):  # Sử dụng range để lặp qua các chỉ số
        ketQua.append(danhSach[i])  # Thêm phần tử gốc vào danh sách kết quả
        if (i+ 1) % n == 0:  # Kiểm tra nếu vị trí chia hết cho n
            ketQua.append('Kteam')  # Thêm "kTeam" vào danh sách kết quả
    return ' '.join(ketQua)  # Kết hợp tất cả các phần tử thành một chuỗi

# Nhập dữ liệu từ bàn phím
danhSach = input('Nhập dữ liệu bất kì: ').split()
if len(danhSach) == 0:
    print('Danh sách rỗng')
else:
    try:
        n = int(input('Nhập số nguyên bất kì: '))
        ketQua = chen_Tu(danhSach, n)
        print(ketQua)
    except ValueError:
        print('Dữ liệu nhập vào chưa hợp lệ')
