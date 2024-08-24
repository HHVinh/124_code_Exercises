def thong_Tin_Tuple(a):
    return max(a), min(a), len(a)

danhSach = input('Nhập danh sách từ bàn phím: ').split()
try:
    tupleSo = tuple(map(float,danhSach))
    soLonNhat, soNhoNhat, soPhanTu = thong_Tin_Tuple(tupleSo)
    print(soLonNhat)
    print(soNhoNhat)
    print(soPhanTu)
except:
    print('Dữ liệu đầu vào không hợp lệ')