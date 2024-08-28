def ds_Hai_Chieu(M,N):
    dsHaiChieu = []
    for i in range(M):
        hang = input(f'Hãy nhập dữ liệu cho hàng {i +1} với {N} giá trị: ').split()
        if len(hang) != N:
            print(f'Bạn cần nhập đúng {N} giá trị')
            return None
        dsHaiChieu.append(hang)
    return dsHaiChieu

def ptu_Chung(dsHaiChieu):
    setHang0 = set(dsHaiChieu[0])
    ptuChung = setHang0.intersection(*[hang for hang in dsHaiChieu])
    return ptuChung

try:
    M,N = map(int,input('Hãy nhập số hàng và số giá trị của mỗi hàng: ').split())
    if M <=0 or N <= 0:
        print('Hãy nhập số nguyên dương cho 2 giá trị')
    else:
        dsHaiChieu = ds_Hai_Chieu(M,N)
        if dsHaiChieu is not None:
            ptuChung = ptu_Chung(dsHaiChieu)
            print('Các phần tử chung của danh sách hai chiều là: ',ptuChung)
except:
    print('Dữ liệu đầu vào chưa hợp lệ')
    
