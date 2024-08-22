def danh_Sach_Hai_Chieu(M,N):
    danhSach = []
    for i in range(M):
        while True:
            hang = input(f'Nhập dữ liệu hàng {i +1 } với {N} giá trị: ').split()
            if len(hang) == N:
                danhSach.append(hang)
                break
            else:
                print(f'Dữ liệu của hàng phải đủ {N} giá trị')
    return danhSach

def danh_Sach_Chuyen_Vi(danhSach):
    soCot = len(danhSach[0])
    soHang = len(danhSach)
    dsChuyenVi = [[] for k in range(soCot)]

    for i in range(soCot):
        for j in range(soHang):
            dsChuyenVi[i].append(danhSach[j][i])
    return dsChuyenVi

try:
    M, N = map(int, input('Nhập số cột và số hàng của danh sách: ').split())
    if M <= 0 or N <= 0:
        print('Vui lòng nhập số nguyên dương')
    else:
        dsHaiChieu = danh_Sach_Hai_Chieu(M,N)
        if dsHaiChieu is not None:
            dsChuyenVi = danh_Sach_Chuyen_Vi(dsHaiChieu)
            for hang in dsChuyenVi:
                print(*hang)
except:
    print('Dữ liệu đầu vào không hợp lệ')