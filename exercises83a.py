def danh_Sach(danhSach,n):
    soPhanTu = len(danhSach)
    soLanLapLai = n // soPhanTu + 1
    danhSachNhanBan = danhSach*soLanLapLai
    ketQua = danhSachNhanBan[:n]
    return ketQua

danhSach = input('Nhập dữ liệu bất kì: ').split()
if len(danhSach) == 0:
    print('Danh sách rỗng')
else:
    try:
        n = int(input('Nhập số bất kì: '))
        ketQua = danh_Sach(danhSach, n)
        print(*ketQua)
    except:
        print('Dữ liệu nhập vào không hợp lệ')