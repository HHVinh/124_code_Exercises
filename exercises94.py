def ds_Hai_Chieu(M,N):
    danhSach =[]
    for i in range(M):
        while True:
            hang = input(f'Hãy nhập dữ liệu dòng thứ {i+1} với {N} giá trị: ').split()
            if len(hang) == N:
                danhSach.append(hang)
                break
    return danhSach

def phan_Tu_Trung(danhSach):
    dsMotChieu = []
    phanTuTrung = []
    for dsCon in danhSach:
        for phanTu in dsCon:
            dsMotChieu.append(phanTu)
    
    for phanTu in dsMotChieu:
        if dsMotChieu.count(phanTu) > 1 and phanTu not in phanTuTrung:
            phanTuTrung.append(phanTu)       
    return phanTuTrung

try:
    M, N = map(int, input('Hãy nhập 2 giá trị cột và hàng bất kì: ').split())
    if M <= 0 or N <= 0:
        print('Hãy nhập hai số nguyên dương')
    else:
        dsHaiChieu = ds_Hai_Chieu(M,N)
        phanTuTrung = phan_Tu_Trung(dsHaiChieu)
        print('Các phần tử trùng nhau trong danh sách là: ',' '.join(phanTuTrung))
except:
    print('Dữ liệu đầu vào không lệ')
