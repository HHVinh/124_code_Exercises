def danh_Sach_Hai_Chieu(M,N):
    danhSach = []
    for i in range(M):
        while True:
            hang = input(f'Hãy nhập dữ liệu hàng {i+1} với {N} giá trị: ').split()
            if len(hang) == N:
                danhSach.append(hang)
                break
            else:
                print('Bạn đã nhập sai yêu cầu')
    return danhSach

def phan_Tu_Dai_Nhat(danhSach):
    ketQua = []
    for hang in danhSach:
        # Tìm phần tử có độ dài lớn nhất trong danh sách con
        phanTuMax = max(hang, key=len)
        ketQua.append(phanTuMax)
    return ketQua

def phan_Tu_Dai_Nhat_Moi_Hang(danhSach):
    return ' '.join(phan_Tu_Dai_Nhat(danhSach))
    
try:
    M, N = map(int, input('Nhập lần lượt 2 số M và N cách nhau bởi khỏang trắng: ').split())
    danhSach = danh_Sach_Hai_Chieu(M,N)
    ketQua = phan_Tu_Dai_Nhat_Moi_Hang(danhSach)
    print(ketQua)
except:
    print('Dữ liệu đầu vào chưa hợp lệ')
