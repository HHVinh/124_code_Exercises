def nhan_Hai_Danh_Sach(dong1, dong2):
    ketQua = [dong1[i] * dong2[-(i+1)] for i in range(len(dong1))]
    return ketQua

dong1 = input('Nhập danh sách thứ nhất: ').split()
dong2 = input('Nhập danh sách thứ hai: ').split()

if len(dong1) < 0 or len(dong1) != len(dong2):
    print('Danh sách cả hai dòng không khớp nhau:')

else:
    try:
        dsDong1 = list(map(float,dong1))
        dsDong2 = list(map(float,dong2))
        ketQua = nhan_Hai_Danh_Sach(dsDong1,dsDong2)
        print(*ketQua)
    except:
        print('Dữ liệu đầu vào chưa hợp lệ')

